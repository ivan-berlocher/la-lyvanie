"""
Sensemaking Step — Intent extraction
Converts normalized input to UIL (Universal Intent Language).
This is where the LLM is called for intent parsing.
"""

from pydantic import BaseModel
from typing import Optional
import json
import re

from uil import Intent, Constraint, Provenance
from .perception import PerceptionOutput


class SensemakingOutput(BaseModel):
    """Output of sensemaking: a structured UIL intent."""
    intent: Intent
    raw_llm_response: Optional[str] = None
    parsing_notes: list[str] = []


class SensemakingStep:
    """
    S in PSMR — Sensemaking
    Extracts structured intent from normalized input.
    """
    
    def __init__(self, llm_provider: str = "openai"):
        self.llm_provider = llm_provider
        self.model_name = "gpt-4o" if llm_provider == "openai" else "mock"
    
    async def process(
        self,
        perception: PerceptionOutput,
        llm_client,
        context: Optional[dict] = None
    ) -> SensemakingOutput:
        """Extract UIL intent from perception output."""
        
        prompt = self._build_extraction_prompt(perception.normalized_content, context)
        
        # Call LLM
        llm_response = await llm_client.generate(prompt)
        
        # Parse response to UIL
        intent = self._parse_to_uil(
            llm_response,
            perception.normalized_content
        )
        
        return SensemakingOutput(
            intent=intent,
            raw_llm_response=llm_response,
            parsing_notes=[f"Extracted from: {perception.normalized_content[:50]}..."]
        )
    
    def _build_extraction_prompt(self, content: str, context: Optional[dict]) -> str:
        """Build the prompt for intent extraction."""
        
        context_str = ""
        if context and context.get("previous_goal"):
            context_str = f"\nPrevious goal: {context['previous_goal']}"
        
        return f"""Extract the user's intent from the following input.

Input: "{content}"{context_str}

Return a JSON object with:
- type: one of ACTION, QUERY, PLAN, REFLECT
- goal: the user's goal in a clear sentence
- domain: the domain (travel, productivity, research, etc.)
- verb: the main action verb
- entities: list of key entities mentioned
- constraints: list of constraints with type (temporal, budget, spatial, resource), key, and value
- confidence: your confidence in this interpretation (0.0 to 1.0)

Return ONLY valid JSON, no explanation."""
    
    def _parse_to_uil(self, llm_response: str, original_input: str) -> Intent:
        """Parse LLM response to UIL Intent."""
        
        try:
            # Try to extract JSON from response
            json_match = re.search(r'\{[\s\S]*\}', llm_response)
            if json_match:
                data = json.loads(json_match.group())
            else:
                raise ValueError("No JSON found in response")
            
            # Build constraints
            constraints = []
            for c in data.get("constraints", []):
                if isinstance(c, dict) and "type" in c:
                    constraints.append(Constraint(
                        type=c.get("type", "resource"),
                        key=c.get("key", "unknown"),
                        value=c.get("value", "")
                    ))
            
            return Intent(
                type=data.get("type", "ACTION"),
                goal=data.get("goal", original_input),
                domain=data.get("domain"),
                verb=data.get("verb"),
                entities=data.get("entities", []),
                constraints=constraints,
                confidence=float(data.get("confidence", 0.5)),
                provenance=Provenance(
                    agent="IntentParser",
                    model=self.model_name
                )
            )
            
        except (json.JSONDecodeError, ValueError) as e:
            # Fallback: create basic intent from input
            return Intent(
                type="ACTION",
                goal=original_input,
                confidence=0.3,
                status="uncertain",
                provenance=Provenance(
                    agent="IntentParser",
                    model=self.model_name
                )
            )
