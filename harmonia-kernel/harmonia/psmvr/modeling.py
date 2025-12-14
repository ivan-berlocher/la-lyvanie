from __future__ import annotations
from typing import Any, Dict
import time
from ..pir.schema import Plan, PlanStep, Provenance
from .trace import new_uuid, now_iso

def model(uil: Dict[str, Any]) -> Dict[str, Any]:
    t0 = time.time()
    intent_id = uil["intent_id"]
    entities = uil.get("entities", [])
    city = next((e for e in entities if e[0].isalpha() and e.lower() not in ("trip",)), None)
    duration_days = None
    budget = None
    for c in uil.get("constraints", []):
        if c["type"]=="temporal" and c["key"]=="duration_days":
            try: duration_days = int(c["value"])
            except: pass
        if c["type"]=="budget" and c["key"]=="total":
            try: budget = float(c["value"])
            except: pass

    steps = []
    steps.append(PlanStep(
        step_id=new_uuid(),
        order=1,
        action_type="research",
        description=f"Collect 3 accommodation options in {city or 'target city'}",
        inputs=[city] if city else [],
        outputs=["accommodation_options"],
        resources=["web"],
        dependencies=[],
        estimated_effort="medium",
    ))
    steps.append(PlanStep(
        step_id=new_uuid(),
        order=2,
        action_type="draft_itinerary",
        description=f"Draft a {duration_days or 'multi'}-day itinerary in {city or 'target city'}",
        inputs=["accommodation_options"],
        outputs=["itinerary"],
        resources=["planner"],
        dependencies=[steps[0].step_id],
        estimated_effort="medium",
    ))
    steps.append(PlanStep(
        step_id=new_uuid(),
        order=3,
        action_type="budget_check",
        description="Estimate total cost and ensure budget constraints are satisfied",
        inputs=["itinerary"],
        outputs=["total_cost_estimate"],
        resources=["calculator"],
        dependencies=[steps[1].step_id],
        estimated_effort="low",
    ))

    # naive estimate: 150/day + 100 fixed
    est = None
    if duration_days:
        est = 100 + 150*duration_days
    prov = Provenance(agent="modeling", model=None, timestamp=now_iso(), trace_id="")
    plan = Plan(
        plan_id=new_uuid(),
        intent_id=intent_id,
        steps=steps,
        assumptions=["Prices are approximate; availability not checked."],
        total_cost_estimate=est,
        provenance=prov,
    )
    dt_ms = int((time.time()-t0)*1000)
    return {"plan": plan.model_dump(), "duration_ms": dt_ms}
