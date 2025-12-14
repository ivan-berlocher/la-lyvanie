"""Intent Parser Agent - Transforms natural language to UIL Intent.

Production guardrails:
- Uses OpenAI Structured Outputs for strict JSON schema
- Automatic fallback to mock on LLM failure
- Deterministic mode (temperature=0) for reproducible demos
"""

import json
import re
from typing import Any, Literal

from .base import AgentResult, AgentStatus, BaseAgent
from uil.schema import Constraint, Intent, Provenance
from llm.provider import UIL_INTENT_SCHEMA


class IntentParserAgent(BaseAgent):
    """
    Parses natural language input into a structured UIL Intent.
    
    This is the first agent in the pipeline - it demonstrates
    that we're not just prompting, but creating structured
    intermediate representations.
    
    LLM-powered (when available) for richer entity/constraint extraction.
    Falls back to deterministic mock if LLM fails.
    """

    name = "IntentParser"
    description = "Transforms natural language to UIL Intent schema"

    SYSTEM_PROMPT = """You are an intent parser for a cognitive kernel.

Your job is to classify user input into COGNITIVE PRIMITIVES (not business domains).
These are fundamental operations of thought, applicable to any subject.

COGNITIVE PRIMITIVES:
- PLAN: Organize action in time (scheduling, roadmaps, sequences)
- DECIDE: Choose between options (comparison, trade-offs, selection)
- ANALYZE: Understand or explain a situation (diagnosis, breakdown, patterns)
- SOLVE: Resolve a problem (troubleshooting, optimization, finding solutions)
- LEARN: Acquire knowledge (explanation, teaching, discovery, "how does X work")
- EXECUTE: Perform a concrete action (do, create, send, make)
- CLARIFY: Resolve ambiguity (questions about specifics, requirements, definitions)

Extract:
1. intent_type: The cognitive primitive (PLAN, DECIDE, ANALYZE, SOLVE, LEARN, EXECUTE, CLARIFY)
2. goal: The core objective (clear, actionable statement)
3. domain: The subject area (e.g., "phd", "travel", "finance", "health", "software")
4. entities: Named things mentioned (people, places, concepts, tools, dates)
5. constraints: Limitations or conditions (time, resource, preference)

KEY INSIGHT: The domain changes, but the cognition stays the same.
"Plan my PhD application" and "Plan my vacation" are both PLAN — different domains, same cognitive operation.

Be precise. If uncertain, lower confidence. If ambiguous, use CLARIFY."""

    async def execute(self, input_data: str, context: dict[str, Any] = None) -> AgentResult:
        """Parse user input into UIL Intent."""
        context = context or {}
        used_fallback = False

        if not input_data or not input_data.strip():
            return AgentResult(
                agent_name=self.name,
                status=AgentStatus.ERROR,
                output=None,
                confidence=0.0,
                reasoning="Empty input provided",
            )

        try:
            # Use LLM with strict JSON schema if available
            if self.llm and self.llm.name != "mock":
                try:
                    parsed = await self._parse_with_llm(input_data)
                except Exception as llm_error:
                    # Fallback to mock on ANY LLM failure (timeout, invalid JSON, etc.)
                    print(f"[IntentParser] LLM failed ({llm_error}), falling back to mock")
                    parsed = self._mock_parse(input_data)
                    used_fallback = True
            else:
                # Mock parsing for demo without LLM or with MockProvider
                parsed = self._mock_parse(input_data)

            # Build UIL Intent from parsed data
            intent = self._build_intent(parsed)

            return AgentResult(
                agent_name=self.name,
                status=AgentStatus.SUCCESS,
                output=intent.model_dump(),
                confidence=parsed.get("confidence", 0.5),
                reasoning=parsed.get("reasoning", "Intent parsed successfully") + 
                         (" [fallback: mock]" if used_fallback else ""),
                metadata={
                    "raw_parse": parsed,
                    "used_fallback": used_fallback,
                    "model": self.llm.current_model if self.llm else "mock"
                },
            )

        except Exception as e:
            return AgentResult(
                agent_name=self.name,
                status=AgentStatus.ERROR,
                output=None,
                confidence=0.0,
                reasoning=f"Parse error: {str(e)}",
            )

    async def _parse_with_llm(self, input_data: str) -> dict:
        """Parse using LLM with strict JSON schema enforcement."""
        # Use complete_json for OpenAI (Structured Outputs)
        if hasattr(self.llm, 'complete_json'):
            return await self.llm.complete_json(
                system=self.SYSTEM_PROMPT,
                user=f"Parse this input:\n\n{input_data}",
                schema=UIL_INTENT_SCHEMA,
                schema_name="uil_intent"
            )
        else:
            # Fallback for providers without structured outputs
            response = await self.llm.complete(
                system=self.SYSTEM_PROMPT,
                user=f"Parse this input and respond with valid JSON only:\n\n{input_data}",
            )
            return self._extract_json(response)

    def _build_intent(self, parsed: dict) -> Intent:
        """Build UIL Intent from parsed data."""
        # Map constraint types to valid literals
        constraint_type_map = {
            "temporal": "temporal",
            "resource": "resource", 
            "preference": "priority",
            "dependency": "resource",
            "budget": "budget",
            "spatial": "spatial",
            "priority": "priority",
        }
        
        constraints = []
        for c in parsed.get("constraints", []):
            c_type = c.get("type", "priority")
            mapped_type = constraint_type_map.get(c_type, "priority")
            constraints.append(
                Constraint(
                    type=mapped_type,
                    key=c.get("key", c_type),
                    value=c.get("value", "")
                )
            )
        
        return Intent(
            type=parsed.get("intent_type", "EXECUTE"),
            goal=parsed.get("goal", ""),
            domain=parsed.get("domain", "general"),
            entities=parsed.get("entities", []),
            constraints=constraints,
            confidence=parsed.get("confidence", 0.5),
            provenance=Provenance(
                agent=self.name,
                model=self.llm.current_model if self.llm else "mock",
            ),
        )

    def _extract_json(self, text: str) -> dict:
        """Extract JSON from LLM response."""
        # Try direct parse first
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

        # Look for JSON block in markdown
        json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(1))

        # Look for raw JSON object
        json_match = re.search(r"\{.*\}", text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(0))

        raise ValueError("No valid JSON found in response")

    def _mock_parse(self, input_data: str) -> dict:
        """Mock parsing for demo without LLM.
        
        Uses cognitive primitives — domain-agnostic classification.
        """
        input_lower = input_data.lower()

        # =================================================================
        # COGNITIVE PRIMITIVE DETECTION
        # The domain changes, but the cognition stays the same.
        # =================================================================
        
        # PLAN: Organize action in time
        if any(w in input_lower for w in ["plan", "schedule", "organize", "roadmap", "timeline", "prepare"]):
            intent_type = "PLAN"
            reasoning = "Temporal organization detected"
        
        # DECIDE: Choose between options
        elif any(w in input_lower for w in ["decide", "choose", "whether", "should i", "or", "compare", "vs", "better"]):
            intent_type = "DECIDE"
            reasoning = "Decision/comparison pattern detected"
        
        # ANALYZE: Understand / explain
        elif any(w in input_lower for w in ["analyze", "understand", "explain", "why", "what caused", "breakdown", "risks"]):
            intent_type = "ANALYZE"
            reasoning = "Analysis/explanation pattern detected"
        
        # SOLVE: Resolve a problem
        elif any(w in input_lower for w in ["solve", "fix", "resolve", "troubleshoot", "debug", "problem", "issue"]):
            intent_type = "SOLVE"
            reasoning = "Problem-solving pattern detected"
        
        # LEARN: Acquire knowledge
        elif any(w in input_lower for w in ["learn", "how does", "what is", "explain", "teach", "understand", "?"]):
            intent_type = "LEARN"
            reasoning = "Knowledge acquisition pattern detected"
        
        # CLARIFY: Resolve ambiguity
        elif any(w in input_lower for w in ["clarify", "what do you mean", "specify", "which", "exactly", "requirements"]):
            intent_type = "CLARIFY"
            reasoning = "Ambiguity resolution pattern detected"
        
        # EXECUTE: Default to action
        else:
            intent_type = "EXECUTE"
            reasoning = "Concrete action pattern detected"

        # =================================================================
        # DOMAIN INFERENCE
        # =================================================================
        domain = "general"
        domain_keywords = {
            "phd": ["phd", "thesis", "research", "professor", "university", "eth", "epfl", "academic"],
            "travel": ["trip", "vacation", "flight", "hotel", "travel", "visit", "tour"],
            "finance": ["budget", "money", "cost", "invest", "salary", "expense", "payment"],
            "health": ["health", "exercise", "diet", "doctor", "medical", "fitness"],
            "software": ["code", "app", "software", "program", "develop", "build", "api"],
            "career": ["job", "career", "interview", "resume", "application", "work"],
        }
        for d, keywords in domain_keywords.items():
            if any(kw in input_lower for kw in keywords):
                domain = d
                break

        # Extract simple entities (capitalized words)
        entities = re.findall(r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b", input_data)

        # Detect constraints
        constraints = []
        if any(w in input_lower for w in ["today", "tomorrow", "by", "before", "after", "december", "january"]):
            time_match = re.search(r"(today|tomorrow|by \w+|before \w+|after \w+|december|january|february)", input_lower)
            if time_match:
                constraints.append({"type": "temporal", "key": "deadline", "value": time_match.group(1)})

        if any(w in input_lower for w in ["simple", "quick", "easy", "minimal"]):
            constraints.append({"type": "priority", "key": "complexity", "value": "low"})

        return {
            "intent_type": intent_type,
            "goal": input_data.strip(),
            "domain": domain,
            "entities": entities[:5],  # Limit entities
            "constraints": constraints,
            "confidence": 0.75,
            "reasoning": f"[Mock] {reasoning} | Domain: {domain} | {len(entities)} entities",
        }
