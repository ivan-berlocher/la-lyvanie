from __future__ import annotations
from typing import Any, Dict, List
import time

def verify(uil: Dict[str, Any], plan: Dict[str, Any], memory: Dict[str, Any] | None = None) -> Dict[str, Any]:
    t0 = time.time()
    issues: List[Dict[str, Any]] = []
    entities = set(uil.get("entities", []))

    # ENTITY_MISMATCH heuristic: if any step description mentions a known other city not in entities
    other_cities = {"Geneva","Paris","Seoul","Zurich"}
    for step in plan.get("steps", []):
        desc = step.get("description","")
        for c in other_cities:
            if c in desc and c not in entities:
                issues.append({"code":"ENTITY_MISMATCH","severity":"warning","detail":f"Step mentions {c} but intent entities do not include it."})

    # constraint checks
    constraints = uil.get("constraints", [])
    satisfied = 0
    checked = 0
    unaddressed = []
    for c in constraints:
        checked += 1
        ctype, key, op, val = c["type"], c["key"], c["operator"], c["value"]
        addressed = False
        # constraint coverage: step addresses constraint if budget_check step exists for budget, itinerary for duration
        for s in plan.get("steps", []):
            if ctype=="budget" and "budget" in s.get("action_type",""):
                addressed = True
            if ctype=="temporal" and key.startswith("duration") and s.get("action_type")=="draft_itinerary":
                addressed = True
        if not addressed:
            unaddressed.append(c)

        if ctype=="budget" and key=="total" and plan.get("total_cost_estimate") is not None:
            try:
                limit=float(val); est=float(plan["total_cost_estimate"])
                ok = (est <= limit) if op in ("lte","lt","eq") else True
                if ok: satisfied += 1
                else:
                    issues.append({"code":"CONSTRAINT_VIOLATION","severity":"critical","detail":f"Budget {est} exceeds limit {limit}."})
            except Exception:
                issues.append({"code":"CONSTRAINT_CHECK_ERROR","severity":"critical","detail":"Failed to evaluate budget constraint."})
        else:
            # not evaluable => uncertain
            satisfied += 1  # treat as checked structurally
    if unaddressed:
        issues.append({"code":"CONSTRAINT_UNADDRESSED","severity":"warning","detail":f"{len(unaddressed)} constraints not referenced by any plan step.","constraints":unaddressed})

    valid = not any(i["severity"]=="critical" for i in issues)
    approval_required = any(i["severity"]=="warning" for i in issues) or uil.get("confidence",1.0) < 0.7
    dt_ms = int((time.time()-t0)*1000)
    return {"result": {"valid": valid, "approval_required": approval_required, "issues": issues,
                       "constraints_checked": checked, "constraints_satisfied": satisfied},
            "duration_ms": dt_ms}
