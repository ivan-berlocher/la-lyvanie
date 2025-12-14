"""Verifier Agent - Validates plans and detects conflicts."""

import json
import re
from typing import Any

from .base import AgentResult, AgentStatus, BaseAgent


class VerifierAgent(BaseAgent):
    """
    Validates execution plans and detects conflicts.
    
    This agent demonstrates the multi-agent conflict detection
    that proves we're doing more than prompting. It can flag:
    - Constraint violations
    - Resource conflicts
    - Logical inconsistencies
    - Uncertainty requiring human input
    """

    name = "Verifier"
    description = "Validates plans, detects conflicts, ensures constraint satisfaction"

    SYSTEM_PROMPT = """You are a verification agent for a cognitive assistant.
Your role is to critically analyze plans and detect issues.

Given an intent and plan, output JSON:
{
    "valid": boolean,
    "confidence": 0.0-1.0,
    "issues": [
        {
            "severity": "critical|warning|info",
            "type": "constraint_violation|resource_conflict|logical_error|ambiguity|missing_info",
            "description": "string",
            "affected_steps": [step_ids],
            "suggestion": "how to resolve"
        }
    ],
    "conflicts_with_memory": [
        {
            "memory_node": "node_id",
            "conflict_type": "contradicts|supersedes|requires_update",
            "description": "string"
        }
    ],
    "approval_required": boolean,
    "approval_reason": "why human should review (if needed)",
    "reasoning": "overall assessment"
}

Be thorough. Look for edge cases. If uncertain, flag for human review."""

    # Thresholds for demo
    CONFIDENCE_THRESHOLD = 0.6
    MAX_STEPS_WITHOUT_VALIDATION = 5

    async def execute(self, input_data: dict[str, Any], context: dict[str, Any] = None) -> AgentResult:
        """Verify plan against intent and memory."""
        context = context or {}

        if not input_data:
            return AgentResult(
                agent_name=self.name,
                status=AgentStatus.ERROR,
                output=None,
                confidence=0.0,
                reasoning="No data provided for verification",
            )

        try:
            intent = input_data.get("intent", {})
            plan = input_data.get("plan", {})
            memory_snapshot = context.get("memory_snapshot", {})

            # Use LLM for verification - but use mock if it's MockProvider
            if self.llm and self.llm.name != "mock":
                prompt = f"""Verify this plan against the intent:

Intent:
{json.dumps(intent, indent=2)}

Plan:
{json.dumps(plan, indent=2)}

Memory Context:
{json.dumps(memory_snapshot, indent=2)}

Check for issues, conflicts, and whether human approval is needed."""

                response = await self.llm.complete(
                    system=self.SYSTEM_PROMPT,
                    user=prompt,
                )
                verification = self._extract_json(response)
            else:
                # Mock verification for demo
                verification = self._mock_verify(intent, plan, memory_snapshot)

            # Determine status based on verification
            if not verification.get("valid", True):
                status = AgentStatus.CONFLICT
            elif verification.get("approval_required"):
                status = AgentStatus.UNCERTAIN
            elif verification.get("issues"):
                status = AgentStatus.PARTIAL
            else:
                status = AgentStatus.SUCCESS

            # Extract conflicts for result
            conflicts = [
                f"{issue['type']}: {issue['description']}"
                for issue in verification.get("issues", [])
                if issue.get("severity") in ("critical", "warning")
            ]

            return AgentResult(
                agent_name=self.name,
                status=status,
                output=verification,
                confidence=verification.get("confidence", 0.5),
                reasoning=verification.get("reasoning", "Verification complete"),
                conflicts=conflicts,
                metadata={
                    "issue_count": len(verification.get("issues", [])),
                    "memory_conflicts": len(verification.get("conflicts_with_memory", [])),
                    "requires_approval": verification.get("approval_required", False),
                },
            )

        except Exception as e:
            return AgentResult(
                agent_name=self.name,
                status=AgentStatus.ERROR,
                output=None,
                confidence=0.0,
                reasoning=f"Verification error: {str(e)}",
            )

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

    def _mock_verify(
        self,
        intent: dict,
        plan: dict,
        memory_snapshot: dict,
    ) -> dict:
        """Mock verification for demo - generates realistic issues."""
        issues = []
        memory_conflicts = []
        approval_required = False
        approval_reason = ""

        # Check 1: Intent confidence
        intent_confidence = intent.get("confidence", 0.5)
        if intent_confidence < self.CONFIDENCE_THRESHOLD:
            issues.append({
                "severity": "warning",
                "type": "ambiguity",
                "description": f"Intent confidence ({intent_confidence:.2f}) below threshold ({self.CONFIDENCE_THRESHOLD})",
                "affected_steps": [],
                "suggestion": "Consider clarifying the user's goal before proceeding",
            })
            approval_required = True
            approval_reason = "Low confidence intent requires human confirmation"

        # Check 2: Plan step count
        steps = plan.get("steps", [])
        if len(steps) > self.MAX_STEPS_WITHOUT_VALIDATION:
            issues.append({
                "severity": "info",
                "type": "logical_error",
                "description": f"Plan has {len(steps)} steps - consider simplification",
                "affected_steps": list(range(len(steps))),
                "suggestion": "Break into smaller sub-plans or validate intermediate results",
            })

        # Check 3: Constraint validation
        constraints = intent.get("constraints", [])
        for constraint in constraints:
            if constraint.get("type") == "temporal":
                # Check if plan has time-dependent steps
                time_sensitive_steps = [
                    s["step_id"] for s in steps
                    if "schedule" in s.get("action", "").lower()
                    or "timeline" in s.get("action", "").lower()
                ]
                if not time_sensitive_steps and "today" in constraint.get("value", "").lower():
                    issues.append({
                        "severity": "warning",
                        "type": "constraint_violation",
                        "description": f"Temporal constraint '{constraint.get('value')}' may not be satisfiable",
                        "affected_steps": [],
                        "suggestion": "Add explicit scheduling step or adjust timeline",
                    })

        # Check 4: Entity consistency with memory
        intent_entities = set(intent.get("entities", []))
        raw_nodes = memory_snapshot.get("nodes", [])
        
        # Extract node IDs from memory (nodes can be tuples, dicts, or strings)
        memory_node_ids = set()
        for node in raw_nodes:
            if isinstance(node, str):
                memory_node_ids.add(node)
            elif isinstance(node, tuple) and len(node) > 0:
                memory_node_ids.add(str(node[0]))
            elif isinstance(node, dict) and "id" in node:
                memory_node_ids.add(str(node["id"]))
        
        # Find entities that might conflict with existing memory
        if memory_node_ids and intent_entities:
            for entity in intent_entities:
                # Simulate finding a conflict (for demo purposes)
                if entity.lower() in [n.lower() for n in memory_node_ids if isinstance(n, str)]:
                    memory_conflicts.append({
                        "memory_node": entity,
                        "conflict_type": "requires_update",
                        "description": f"Entity '{entity}' exists in memory - plan may need to account for existing context",
                    })

        # Check 5: Risk assessment
        plan_risks = plan.get("risks", [])
        if plan_risks:
            for risk in plan_risks[:2]:  # Limit to 2 risks
                issues.append({
                    "severity": "info",
                    "type": "missing_info",
                    "description": f"Identified risk: {risk}",
                    "affected_steps": [],
                    "suggestion": "Consider mitigation strategy",
                })

        # Check 6: High-effort steps
        high_effort_steps = [s for s in steps if s.get("estimated_effort") == "high"]
        if len(high_effort_steps) > 2:
            issues.append({
                "severity": "warning",
                "type": "resource_conflict",
                "description": f"{len(high_effort_steps)} high-effort steps may exceed capacity",
                "affected_steps": [s["step_id"] for s in high_effort_steps],
                "suggestion": "Consider parallelization or breaking into phases",
            })

        # Determine overall validity
        critical_issues = [i for i in issues if i.get("severity") == "critical"]
        valid = len(critical_issues) == 0

        # Calculate confidence based on issues
        base_confidence = 0.9
        confidence = base_confidence - (len(issues) * 0.1) - (len(memory_conflicts) * 0.05)
        confidence = max(0.3, min(1.0, confidence))

        return {
            "valid": valid,
            "confidence": confidence,
            "issues": issues,
            "conflicts_with_memory": memory_conflicts,
            "approval_required": approval_required,
            "approval_reason": approval_reason,
            "reasoning": f"Verification complete: {len(issues)} issues found, {'valid' if valid else 'invalid'} plan",
        }
