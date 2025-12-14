from __future__ import annotations
from typing import Any, Dict
import time

def respond(uil: Dict[str, Any], plan: Dict[str, Any], verification: Dict[str, Any]) -> Dict[str, Any]:
    t0 = time.time()
    res = verification["result"]
    if not res["valid"]:
        msg = "I cannot proceed: the proposed plan violates one or more critical constraints."
    elif res["approval_required"]:
        msg = "Plan prepared, but approval is required due to warnings/uncertainty."
    else:
        msg = "Plan verified and ready."

    steps = plan.get("steps", [])
    lines = [msg, "", f"Goal: {uil.get('goal')}", "Steps:"]
    for s in sorted(steps, key=lambda x: x.get("order",0)):
        lines.append(f"{s.get('order')}. {s.get('description')}")
    if plan.get("total_cost_estimate") is not None:
        lines.append(f"Estimated total cost: {plan['total_cost_estimate']}")
    out = {"message": "\n".join(lines), "status": ("rejected" if not res["valid"] else ("approval_required" if res["approval_required"] else "accepted"))}
    dt_ms = int((time.time()-t0)*1000)
    return {"output": out, "duration_ms": dt_ms}
