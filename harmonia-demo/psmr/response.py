"""
Response Step — Action execution and output generation.
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from .modeling import ModelingOutput


class ResponseOutput(BaseModel):
    """Final response to user."""
    response_text: str
    action_taken: str
    success: bool
    confidence: float
    warnings: list[str] = []
    timestamp: datetime = None
    
    def __init__(self, **data):
        super().__init__(**data)
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()


class ResponseStep:
    """
    R in PSMR — Response
    Generates final response and executes actions.
    """
    
    async def generate(
        self,
        intent: dict,
        plan: dict,
        verification: dict = None,
    ) -> str:
        """Generate a simple response based on intent, plan, and verification."""
        verification = verification or {}
        
        goal = intent.get("goal", "your request")
        intent_type = intent.get("type", "ACTION")
        entities = intent.get("entities", [])
        confidence = intent.get("confidence", 0.5)
        
        steps = plan.get("steps", [])
        plan_confidence = plan.get("confidence", 0.5)
        
        issues = verification.get("issues", [])
        is_valid = verification.get("valid", True)
        approval_needed = verification.get("approval_required", False)
        
        # Build response based on context
        response_parts = []
        
        # Intent acknowledgment
        response_parts.append(f"**Goal understood**: {goal}")
        response_parts.append(f"**Type**: {intent_type} | **Confidence**: {confidence:.0%}")
        
        if entities:
            response_parts.append(f"**Entities**: {', '.join(entities)}")
        
        # Plan summary
        if steps:
            response_parts.append(f"\n**Plan** ({len(steps)} steps, {plan_confidence:.0%} confidence):")
            for step in steps[:5]:  # Limit to 5 steps for display
                action = step.get("action", "Step")
                effort = step.get("estimated_effort", "medium")
                response_parts.append(f"  • {action} [{effort}]")
        
        # Verification status
        if issues:
            critical = [i for i in issues if i.get("severity") == "critical"]
            warnings = [i for i in issues if i.get("severity") == "warning"]
            
            if critical:
                response_parts.append(f"\n⚠️ **Critical issues**: {len(critical)}")
            if warnings:
                response_parts.append(f"⚡ **Warnings**: {len(warnings)}")
        
        if approval_needed:
            response_parts.append("\n🔒 **Human approval required** before execution")
        elif is_valid:
            response_parts.append("\n✅ **Ready for execution**")
        
        return "\n".join(response_parts)
    
    async def process(
        self,
        modeling: ModelingOutput,
        llm_client
    ) -> ResponseOutput:
        """Generate response based on modeling output."""
        
        warnings = []
        
        # Check for issues
        if modeling.conflict_detected:
            warnings.append("Agent conflict detected — decision may need review")
        
        if modeling.uncertainty_flag:
            warnings.append("Low confidence — interpretation may be incorrect")
        
        # Generate response text
        if modeling.conflict_detected or modeling.uncertainty_flag:
            response_text = await self._generate_clarification_response(
                modeling, llm_client
            )
            success = False
        else:
            response_text = await self._generate_success_response(
                modeling, llm_client
            )
            success = True
        
        # Calculate overall confidence
        agent_confidences = [d.confidence for d in modeling.agent_decisions]
        overall_confidence = (
            sum(agent_confidences) / len(agent_confidences)
            if agent_confidences else modeling.intent.confidence
        )
        
        return ResponseOutput(
            response_text=response_text,
            action_taken=modeling.selected_action,
            success=success,
            confidence=overall_confidence,
            warnings=warnings
        )
    
    async def _generate_success_response(
        self,
        modeling: ModelingOutput,
        llm_client
    ) -> str:
        """Generate a success response."""
        
        prompt = f"""Generate a brief, helpful response for this completed action.

Goal: {modeling.intent.goal}
Action taken: {modeling.selected_action}
Entities involved: {', '.join(modeling.intent.entities)}

Be concise and confirm what was done. Max 2-3 sentences."""
        
        return await llm_client.generate(prompt)
    
    async def _generate_clarification_response(
        self,
        modeling: ModelingOutput,
        llm_client
    ) -> str:
        """Generate a clarification request."""
        
        issues = []
        if modeling.conflict_detected:
            issues.append("conflicting interpretations")
        if modeling.uncertainty_flag:
            issues.append("low confidence in understanding")
        
        prompt = f"""The system needs clarification for this request.

Original goal: {modeling.intent.goal}
Issues: {', '.join(issues)}

Generate a brief, polite clarification request. Ask ONE specific question to resolve the ambiguity. Max 2 sentences."""
        
        return await llm_client.generate(prompt)
