"""Planner Agent - Creates execution plans from UIL Intents.

Production guardrails:
- Uses OpenAI Structured Outputs for strict JSON schema
- Automatic fallback to mock on LLM failure
- Deterministic mode (temperature=0) for reproducible demos
"""

import json
import re
from typing import Any

from .base import AgentResult, AgentStatus, BaseAgent
from uil.schema import Intent
from llm.provider import PLAN_SCHEMA


class PlannerAgent(BaseAgent):
    """
    Creates structured execution plans from UIL Intents.
    
    Demonstrates multi-step reasoning and plan decomposition.
    The plan becomes part of the traceable execution graph.
    
    LLM-powered (when available) for richer step generation.
    Falls back to deterministic mock if LLM fails.
    """

    name = "Planner"
    description = "Decomposes Intent into actionable execution plan"

    SYSTEM_PROMPT = """You are a planning agent for a cognitive assistant.
Given a structured intent, create an execution plan.

Keep plans concrete, actionable, and minimal (3-7 steps ideal).
If intent is unclear, create a clarification plan first."""

    async def execute(self, input_data: dict[str, Any], context: dict[str, Any] = None) -> AgentResult:
        """Create execution plan from Intent."""
        context = context or {}
        used_fallback = False

        if not input_data:
            return AgentResult(
                agent_name=self.name,
                status=AgentStatus.ERROR,
                output=None,
                confidence=0.0,
                reasoning="No intent provided for planning",
            )

        try:
            # Extract intent data
            if isinstance(input_data, Intent):
                intent_dict = input_data.model_dump()
            else:
                intent_dict = input_data

            goal = intent_dict.get("goal", "")
            intent_type = intent_dict.get("type", "ACTION")
            entities = intent_dict.get("entities", [])
            constraints = intent_dict.get("constraints", [])

            # Use LLM with strict JSON schema if available
            if self.llm and self.llm.name != "mock":
                try:
                    plan = await self._plan_with_llm(goal, intent_type, entities, constraints, context)
                except Exception as llm_error:
                    # Fallback to mock on ANY LLM failure
                    print(f"[Planner] LLM failed ({llm_error}), falling back to mock")
                    plan = self._mock_plan(goal, intent_type, entities, constraints)
                    used_fallback = True
            else:
                # Mock planning for demo
                plan = self._mock_plan(goal, intent_type, entities, constraints)

            # Validate plan structure
            if not plan.get("steps"):
                return AgentResult(
                    agent_name=self.name,
                    status=AgentStatus.PARTIAL,
                    output=plan,
                    confidence=0.3,
                    reasoning="Plan created but no concrete steps generated",
                )

            return AgentResult(
                agent_name=self.name,
                status=AgentStatus.SUCCESS,
                output=plan,
                confidence=plan.get("confidence", 0.7),
                reasoning=plan.get("reasoning", "Plan created successfully") +
                         (" [fallback: mock]" if used_fallback else ""),
                metadata={
                    "step_count": len(plan.get("steps", [])),
                    "has_risks": len(plan.get("risks", [])) > 0,
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
                reasoning=f"Planning error: {str(e)}",
            )

    async def _plan_with_llm(self, goal: str, intent_type: str, entities: list, 
                             constraints: list, context: dict) -> dict:
        """Create plan using LLM with strict JSON schema enforcement."""
        prompt = f"""Create an execution plan for:
Goal: {goal}
Type: {intent_type}
Entities: {entities}
Constraints: {json.dumps(constraints)}
Context: {json.dumps(context.get('memory_snapshot', {}))}"""

        # Use complete_json for OpenAI (Structured Outputs)
        if hasattr(self.llm, 'complete_json'):
            return await self.llm.complete_json(
                system=self.SYSTEM_PROMPT,
                user=prompt,
                schema=PLAN_SCHEMA,
                schema_name="execution_plan"
            )
        else:
            # Fallback for providers without structured outputs
            response = await self.llm.complete(
                system=self.SYSTEM_PROMPT,
                user=prompt + "\n\nRespond with valid JSON only.",
            )
            return self._extract_json(response)

    def _extract_json(self, text: str) -> dict:
        """Extract JSON from LLM response."""
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

        json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(1))

        json_match = re.search(r"\{.*\}", text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(0))

        raise ValueError("No valid JSON found in response")

    def _mock_plan(
        self,
        goal: str,
        intent_type: str,
        entities: list[str],
        constraints: list[dict],
    ) -> dict:
        """Mock planning for demo without LLM."""
        import hashlib

        plan_id = hashlib.md5(goal.encode()).hexdigest()[:8]

        # Generate contextual steps based on intent type
        if intent_type == "QUERY":
            steps = [
                {
                    "step_id": 1,
                    "action": "Search knowledge base",
                    "depends_on": [],
                    "estimated_effort": "low",
                    "tools_needed": ["memory_search"],
                    "validation": "Results found or not",
                },
                {
                    "step_id": 2,
                    "action": "Synthesize answer",
                    "depends_on": [1],
                    "estimated_effort": "medium",
                    "tools_needed": ["llm"],
                    "validation": "Answer addresses query",
                },
            ]
        elif intent_type == "PLAN":
            steps = [
                {
                    "step_id": 1,
                    "action": f"Analyze scope: {goal[:50]}",
                    "depends_on": [],
                    "estimated_effort": "medium",
                    "tools_needed": ["reasoning"],
                    "validation": "Scope defined",
                },
                {
                    "step_id": 2,
                    "action": "Identify dependencies",
                    "depends_on": [1],
                    "estimated_effort": "medium",
                    "tools_needed": ["graph_analysis"],
                    "validation": "Dependencies mapped",
                },
                {
                    "step_id": 3,
                    "action": "Create timeline",
                    "depends_on": [1, 2],
                    "estimated_effort": "low",
                    "tools_needed": ["scheduling"],
                    "validation": "Timeline feasible",
                },
                {
                    "step_id": 4,
                    "action": "Validate with constraints",
                    "depends_on": [3],
                    "estimated_effort": "low",
                    "tools_needed": ["constraint_checker"],
                    "validation": "All constraints satisfied",
                },
            ]
        elif intent_type == "REFLECT":
            steps = [
                {
                    "step_id": 1,
                    "action": "Retrieve relevant history",
                    "depends_on": [],
                    "estimated_effort": "low",
                    "tools_needed": ["memory_retrieval"],
                    "validation": "History loaded",
                },
                {
                    "step_id": 2,
                    "action": "Analyze patterns",
                    "depends_on": [1],
                    "estimated_effort": "high",
                    "tools_needed": ["pattern_analysis"],
                    "validation": "Patterns identified",
                },
                {
                    "step_id": 3,
                    "action": "Generate insights",
                    "depends_on": [2],
                    "estimated_effort": "medium",
                    "tools_needed": ["synthesis"],
                    "validation": "Actionable insights produced",
                },
            ]
        else:  # ACTION
            steps = [
                {
                    "step_id": 1,
                    "action": f"Execute: {goal[:40]}",
                    "depends_on": [],
                    "estimated_effort": "medium",
                    "tools_needed": ["action_executor"],
                    "validation": "Action completed",
                },
                {
                    "step_id": 2,
                    "action": "Verify outcome",
                    "depends_on": [1],
                    "estimated_effort": "low",
                    "tools_needed": ["verification"],
                    "validation": "Expected outcome achieved",
                },
            ]

        # Add entity-specific steps if entities present
        if entities:
            steps.insert(
                0,
                {
                    "step_id": 0,
                    "action": f"Load context for: {', '.join(entities[:3])}",
                    "depends_on": [],
                    "estimated_effort": "low",
                    "tools_needed": ["entity_loader"],
                    "validation": "Entity context available",
                },
            )
            # Renumber steps
            for i, step in enumerate(steps):
                step["step_id"] = i + 1
                step["depends_on"] = [d + 1 for d in step["depends_on"] if d > 0]

        risks = []
        if any(c.get("type") == "temporal" for c in constraints):
            risks.append("Time constraint may limit quality")
        if len(entities) > 3:
            risks.append("Multiple entities increase complexity")

        return {
            "plan_id": plan_id,
            "steps": steps,
            "total_steps": len(steps),
            "critical_path": [s["step_id"] for s in steps if not s["depends_on"] or s["depends_on"][-1] == s["step_id"] - 1],
            "confidence": 0.75,
            "risks": risks,
            "reasoning": f"Mock plan for {intent_type} with {len(steps)} steps",
        }
