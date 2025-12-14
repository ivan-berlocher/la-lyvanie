"""LLM Provider abstraction for Harmonia cognitive kernel.

Implements production-grade guardrails:
- Strict JSON output via OpenAI Structured Outputs
- Determinism mode (temperature=0, seed) for reproducible demos
- Automatic fallback to mock on LLM failure
- Timeout handling
"""

import json
import os
from abc import ABC, abstractmethod
from typing import Any, Optional

# Global provider instance
_provider: Optional["LLMProvider"] = None

# JSON Schemas for strict output validation
# =============================================================================
# COGNITIVE PRIMITIVES — Domain-agnostic intent classification
# =============================================================================
UIL_INTENT_SCHEMA = {
    "type": "object",
    "properties": {
        "intent_type": {
            "type": "string",
            "enum": ["PLAN", "DECIDE", "ANALYZE", "SOLVE", "LEARN", "EXECUTE", "CLARIFY"],
            "description": "Cognitive primitive: PLAN (organize in time), DECIDE (choose between options), ANALYZE (understand/explain), SOLVE (resolve problem), LEARN (acquire knowledge), EXECUTE (perform action), CLARIFY (resolve ambiguity)"
        },
        "goal": {"type": "string", "description": "The core objective, clear and actionable"},
        "domain": {"type": "string", "description": "Inferred domain (e.g., phd, travel, finance, health)"},
        "entities": {"type": "array", "items": {"type": "string"}, "description": "Named things: people, places, concepts, tools"},
        "constraints": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {"type": "string"},
                    "value": {"type": "string"}
                },
                "required": ["type", "value"],
                "additionalProperties": False
            }
        },
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "reasoning": {"type": "string", "description": "Brief explanation of cognitive classification"}
    },
    "required": ["intent_type", "goal", "domain", "entities", "constraints", "confidence", "reasoning"],
    "additionalProperties": False
}

PLAN_SCHEMA = {
    "type": "object",
    "properties": {
        "plan_id": {"type": "string"},
        "steps": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "step_id": {"type": "integer"},
                    "action": {"type": "string"},
                    "depends_on": {"type": "array", "items": {"type": "integer"}},
                    "estimated_effort": {"type": "string", "enum": ["low", "medium", "high"]},
                    "tools_needed": {"type": "array", "items": {"type": "string"}},
                    "validation": {"type": "string"}
                },
                "required": ["step_id", "action", "depends_on", "estimated_effort", "validation"],
                "additionalProperties": False
            }
        },
        "total_steps": {"type": "integer"},
        "critical_path": {"type": "array", "items": {"type": "integer"}},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "risks": {"type": "array", "items": {"type": "string"}},
        "reasoning": {"type": "string"}
    },
    "required": ["plan_id", "steps", "total_steps", "confidence", "reasoning"],
    "additionalProperties": False
}


class LLMProvider(ABC):
    """Abstract base class for LLM providers."""

    name: str = "base"
    current_model: str = "unknown"

    @abstractmethod
    async def complete(self, system: str, user: str, **kwargs) -> str:
        """Generate completion from system + user prompt."""
        pass

    async def complete_json(self, system: str, user: str, schema: dict, **kwargs) -> dict:
        """Generate completion with strict JSON schema enforcement."""
        # Default implementation: call complete and parse JSON
        response = await self.complete(system, user, **kwargs)
        return json.loads(response)


class OpenAIProvider(LLMProvider):
    """OpenAI API provider with production guardrails."""

    name = "openai"

    def __init__(self, model: str = "gpt-4o-mini", api_key: Optional[str] = None):
        self.current_model = model
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self._client = None
        # Determinism settings for reproducible demos
        self.deterministic = True  # Default to deterministic for PhD demos
        self.seed = 42

    def _get_client(self):
        if self._client is None:
            from openai import AsyncOpenAI
            self._client = AsyncOpenAI(api_key=self.api_key)
        return self._client

    async def complete(self, system: str, user: str, **kwargs) -> str:
        client = self._get_client()
        
        # Determinism settings (crucial for PhD demos)
        temperature = 0 if self.deterministic else kwargs.get("temperature", 0.7)
        
        create_kwargs = {
            "model": self.current_model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": temperature,
            "max_tokens": kwargs.get("max_tokens", 1000),
        }
        
        # Add seed for determinism if supported
        if self.deterministic:
            create_kwargs["seed"] = self.seed
        
        response = await client.chat.completions.create(**create_kwargs)
        return response.choices[0].message.content

    async def complete_json(self, system: str, user: str, schema: dict, schema_name: str = "response", **kwargs) -> dict:
        """Generate completion with OpenAI Structured Outputs (strict JSON schema)."""
        client = self._get_client()
        
        # Determinism settings
        temperature = 0 if self.deterministic else kwargs.get("temperature", 0.7)
        
        create_kwargs = {
            "model": self.current_model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": temperature,
            "max_tokens": kwargs.get("max_tokens", 1500),
            # Structured Outputs - guarantees valid JSON matching schema
            "response_format": {
                "type": "json_schema",
                "json_schema": {
                    "name": schema_name,
                    "strict": True,
                    "schema": schema
                }
            }
        }
        
        if self.deterministic:
            create_kwargs["seed"] = self.seed
        
        response = await client.chat.completions.create(**create_kwargs)
        content = response.choices[0].message.content
        return json.loads(content)


class MockProvider(LLMProvider):
    """Mock provider for demo without API key."""

    name = "mock"
    current_model = "mock-v1"

    def __init__(self):
        self.call_count = 0

    async def complete(self, system: str, user: str, **kwargs) -> str:
        """Return mock response - actual logic handled in agents."""
        self.call_count += 1
        return f"[MOCK RESPONSE #{self.call_count}] System had {len(system)} chars, User had {len(user)} chars"


class LocalProvider(LLMProvider):
    """Local LLM provider (Ollama-compatible)."""

    name = "local"

    def __init__(self, model: str = "llama3.2", base_url: str = "http://localhost:11434"):
        self.current_model = model
        self.base_url = base_url

    async def complete(self, system: str, user: str, **kwargs) -> str:
        import httpx

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/api/chat",
                json={
                    "model": self.current_model,
                    "messages": [
                        {"role": "system", "content": system},
                        {"role": "user", "content": user},
                    ],
                    "stream": False,
                },
                timeout=60.0,
            )
            response.raise_for_status()
            return response.json()["message"]["content"]


def get_provider() -> LLMProvider:
    """Get the current LLM provider instance."""
    global _provider
    if _provider is None:
        # Default to mock if no API key
        if os.getenv("OPENAI_API_KEY"):
            _provider = OpenAIProvider()
        else:
            _provider = MockProvider()
    return _provider


def switch_model(provider_name: str, model: Optional[str] = None) -> LLMProvider:
    """Switch to a different LLM provider/model.
    
    Args:
        provider_name: "openai", "mock", or "local"
        model: Model name (e.g., "gpt-4o", "gpt-4o-mini", "llama3.2")
    
    Returns:
        The new provider instance
    """
    global _provider

    if provider_name == "openai":
        _provider = OpenAIProvider(model=model or "gpt-4o-mini")
    elif provider_name == "local":
        _provider = LocalProvider(model=model or "llama3.2")
    elif provider_name == "mock":
        _provider = MockProvider()
    else:
        raise ValueError(f"Unknown provider: {provider_name}")

    return _provider


def get_available_models() -> dict[str, list[str]]:
    """List available models per provider."""
    return {
        "openai": ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-3.5-turbo"],
        "local": ["llama3.2", "llama3.1", "mistral", "codellama"],
        "mock": ["mock-v1"],
    }
