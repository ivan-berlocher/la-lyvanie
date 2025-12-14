"""
UIL Schema — Universal Intent Language
Typed intermediate representation for cognitive intent.

The LLM is not used as a reasoning engine.
It is used as a semantic front-end that maps open-ended natural language 
into a fixed set of cognitive intent primitives.
"""

from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime
from uuid import uuid4


# =============================================================================
# COGNITIVE PRIMITIVES (PhD-grade ontology)
# =============================================================================
# These are domain-agnostic cognitive operations, not business logic.
# The same kernel handles any domain through these fixed primitives.

IntentType = Literal[
    "PLAN",      # Organize action in time (scheduling, roadmaps, sequences)
    "DECIDE",    # Choose between options (comparison, trade-offs)
    "ANALYZE",   # Understand / explain a situation (diagnosis, breakdown)
    "SOLVE",     # Resolve a problem (troubleshooting, optimization)
    "LEARN",     # Acquire knowledge (explanation, teaching, discovery)
    "EXECUTE",   # Perform a concrete action (do, create, send)
    "CLARIFY",   # Resolve ambiguity (questions, specifications)
]

# Backward compatibility aliases
INTENT_TYPE_ALIASES = {
    "ACTION": "EXECUTE",
    "QUERY": "LEARN", 
    "REFLECT": "ANALYZE",
    "ASSERT": "EXECUTE",
    "REVOKE": "EXECUTE",
}


class Provenance(BaseModel):
    """Tracks origin of the intent."""
    agent: str
    model: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    trace_id: str = Field(default_factory=lambda: str(uuid4()))


class Constraint(BaseModel):
    """A constraint on the intent."""
    type: Literal["temporal", "budget", "spatial", "resource", "priority"]
    key: str
    value: str | int | float
    operator: Literal["eq", "lt", "gt", "lte", "gte", "contains"] = "eq"


class Intent(BaseModel):
    """
    Universal Intent Language (UIL) schema.
    
    This is the intermediate representation — the star of the demo.
    Maps open-ended natural language to fixed cognitive primitives.
    
    Invariant: For a given input, the UIL schema and verification rules 
    remain identical across models.
    """
    
    # Identity
    intent_id: str = Field(default_factory=lambda: str(uuid4()))
    
    # Core classification — cognitive primitive, not domain
    type: Literal["PLAN", "DECIDE", "ANALYZE", "SOLVE", "LEARN", "EXECUTE", "CLARIFY",
                  # Legacy types (mapped internally)
                  "ACTION", "QUERY", "REFLECT", "ASSERT", "REVOKE"]
    
    # Semantic payload
    goal: str
    domain: Optional[str] = None  # Inferred domain (e.g., "phd", "travel", "finance")
    verb: Optional[str] = None    # Primary action verb
    
    # Entities and constraints
    entities: list[str] = Field(default_factory=list)
    constraints: list[Constraint] = Field(default_factory=list)
    
    # Confidence and status
    confidence: float = Field(ge=0.0, le=1.0, default=0.5)
    status: Literal["pending", "active", "completed", "failed", "uncertain"] = "pending"
    
    # Lineage
    parent_id: Optional[str] = None
    provenance: Provenance = Field(default_factory=lambda: Provenance(agent="system"))
    
    @property
    def cognitive_type(self) -> str:
        """Return the normalized cognitive primitive."""
        return INTENT_TYPE_ALIASES.get(self.type, self.type)
    
    def to_demo_json(self) -> dict:
        """Return clean JSON for demo display."""
        return {
            "intent_id": self.intent_id[:8] + "...",
            "type": self.type,
            "cognitive_primitive": self.cognitive_type,
            "goal": self.goal,
            "domain": self.domain,
            "entities": self.entities,
            "constraints": [
                {"type": c.type, "key": c.key, "value": c.value}
                for c in self.constraints
            ],
            "confidence": round(self.confidence, 2),
            "status": self.status,
            "provenance": {
                "agent": self.provenance.agent,
                "model": self.provenance.model,
                "timestamp": self.provenance.timestamp.isoformat()
            }
        }


# Example usage
if __name__ == "__main__":
    intent = Intent(
        type="PLAN",
        goal="Plan a 3-day trip in Zurich",
        domain="travel",
        verb="plan",
        entities=["Zurich", "hotel", "transport"],
        constraints=[
            Constraint(type="budget", key="max_budget", value=1200),
            Constraint(type="temporal", key="month", value="2025-04")
        ],
        confidence=0.82,
        provenance=Provenance(agent="IntentParser", model="gpt-4o")
    )
    
    import json
    print(json.dumps(intent.to_demo_json(), indent=2))
