from __future__ import annotations
from typing import Any, Dict, Optional
import re, time
from ..uil.schema import Intent, Constraint, Provenance
from .trace import new_uuid, now_iso

def _extract_budget(text: str) -> Optional[float]:
    m = re.search(r"(?:under|<=|≤)\s*([0-9]+(?:\.[0-9]+)?)\s*([A-Za-z]{3})", text, re.IGNORECASE)
    if m:
        return float(m.group(1))
    m2 = re.search(r"budget\s*(?:of|=)?\s*([0-9]+(?:\.[0-9]+)?)", text, re.IGNORECASE)
    if m2:
        return float(m2.group(1))
    return None

def _extract_duration_days(text: str) -> Optional[int]:
    m = re.search(r"(\d+)\s*[- ]?day", text, re.IGNORECASE)
    return int(m.group(1)) if m else None

def _extract_city(text: str) -> Optional[str]:
    # very small heuristic for demo
    for city in ["Zurich","Geneva","Paris","Seoul"]:
        if re.search(rf"\b{re.escape(city)}\b", text, re.IGNORECASE):
            return city
    return None

def sensemake(perception: Dict[str, Any], *, mode: str = "mock", model_name: str = "mock") -> Dict[str, Any]:
    """Return a UIL Intent as dict. mode='mock' is deterministic."""
    t0 = time.time()
    text = perception["text"]
    intent_type = "PLAN" if re.search(r"\bplan\b", text, re.IGNORECASE) else "ANALYZE"
    city = _extract_city(text)
    budget = _extract_budget(text)
    duration = _extract_duration_days(text)

    constraints = []
    entities = []
    if city:
        entities.append(city)
    if "trip" in text.lower():
        entities.append("trip")

    if duration is not None:
        constraints.append(Constraint(type="temporal", key="duration_days", value=duration, operator="eq"))
    if re.search(r"next\s+month", text, re.IGNORECASE):
        constraints.append(Constraint(type="temporal", key="timing", value="next month", operator="eq"))
    if budget is not None:
        constraints.append(Constraint(type="budget", key="total", value=budget, operator="lte"))

    conf = 0.92 if mode == "mock" else 0.80
    prov = Provenance(agent="sensemaking", model=(model_name if mode!="mock" else None),
                      timestamp=now_iso(), trace_id="")  # trace_id filled by caller
    uil = Intent(
        intent_id=new_uuid(),
        type=intent_type,
        goal=(f"Plan a {duration}-day trip to {city}" if (intent_type=="PLAN" and city and duration) else text),
        domain="travel" if city else None,
        verb="plan" if intent_type=="PLAN" else None,
        entities=entities,
        constraints=constraints,
        confidence=conf,
        status="pending",
        provenance=prov,
    )
    dt_ms = int((time.time()-t0)*1000)
    return {"uil": uil.model_dump(), "duration_ms": dt_ms}
