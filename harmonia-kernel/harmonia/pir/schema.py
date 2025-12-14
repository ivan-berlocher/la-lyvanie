from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from typing import List, Optional, Literal, Dict, Any

Effort = Literal["low","medium","high"]

class TimeWindow(BaseModel):
    model_config = ConfigDict(extra="forbid")
    start: Optional[str] = None
    end: Optional[str] = None
    duration: Optional[str] = None

class PlanStep(BaseModel):
    model_config = ConfigDict(extra="forbid")
    step_id: str
    order: int
    action_type: str
    description: str
    inputs: List[str]
    outputs: List[str]
    resources: List[str]
    dependencies: List[str]
    time_window: Optional[TimeWindow] = None
    estimated_effort: Effort

class Provenance(BaseModel):
    model_config = ConfigDict(extra="forbid")
    agent: str
    model: Optional[str] = None
    timestamp: str
    trace_id: str

class Plan(BaseModel):
    model_config = ConfigDict(extra="forbid")
    plan_id: str
    intent_id: str
    steps: List[PlanStep]
    assumptions: List[str]
    total_cost_estimate: Optional[float] = None
    provenance: Provenance
