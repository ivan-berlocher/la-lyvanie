from __future__ import annotations
from pydantic import BaseModel, Field, ConfigDict
from typing import Literal, Optional, List, Any, Dict

IntentType = Literal["PLAN","DECIDE","ANALYZE","SOLVE","LEARN","EXECUTE","CLARIFY"]
ConstraintType = Literal["temporal","budget","spatial","resource","priority"]
Operator = Literal["eq","lt","gt","lte","gte","contains"]
Status = Literal["pending","active","completed","failed","uncertain"]

class Provenance(BaseModel):
    model_config = ConfigDict(extra="forbid")
    agent: str
    model: Optional[str] = None
    timestamp: str
    trace_id: str

class Constraint(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: ConstraintType
    key: str
    value: Any
    operator: Operator

class Intent(BaseModel):
    model_config = ConfigDict(extra="forbid")
    intent_id: str
    type: IntentType
    goal: str
    domain: Optional[str] = None
    verb: Optional[str] = None
    entities: List[str]
    constraints: List[Constraint]
    confidence: float = Field(ge=0.0, le=1.0)
    status: Status
    parent_id: Optional[str] = None
    provenance: Provenance
