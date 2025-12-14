from __future__ import annotations
from typing import Any, Dict
from .trace import Trace
from .perception import perceive
from .sensemaking import sensemake
from .modeling import model as model_stage
from .verification import verify
from .response import respond

def run(input_text: str, *, mode: str = "mock", model_name: str = "mock") -> Dict[str, Any]:
    trace = Trace()

    # P
    p_out = perceive(input_text)
    trace.append("P", {"raw": input_text}, p_out, "processed", 5, {"agent":"perception"}, {})

    # S
    s = sensemake(p_out, mode=mode, model_name=model_name)
    uil = s["uil"]
    uil["provenance"]["trace_id"] = trace.trace_id
    trace.append("S", p_out, uil, "processed", s["duration_ms"], {"agent":"sensemaking","model": (model_name if mode!="mock" else "mock")}, {"intent_id": uil["intent_id"]})

    # M
    m = model_stage(uil)
    plan = m["plan"]
    plan["provenance"]["trace_id"] = trace.trace_id
    trace.append("M", uil, plan, "processed", m["duration_ms"], {"agent":"modeling"}, {"intent_id": uil["intent_id"], "plan_id": plan["plan_id"]})

    # V
    v = verify(uil, plan, memory={})
    decision = "accepted" if v["result"]["valid"] and not v["result"]["approval_required"] else ("approval_required" if v["result"]["valid"] else "rejected")
    trace.append("V", plan, v["result"], decision, v["duration_ms"], {"agent":"verifier"}, {"intent_id": uil["intent_id"], "plan_id": plan["plan_id"]},
                 {"constraints_checked": v["result"]["constraints_checked"], "constraints_satisfied": v["result"]["constraints_satisfied"], "issues": v["result"]["issues"]})

    # R
    r = respond(uil, plan, v)
    trace.append("R", v["result"], r["output"], r["output"]["status"], r["duration_ms"], {"agent":"response"}, {"intent_id": uil["intent_id"], "plan_id": plan["plan_id"]})

    return {
        "uil": uil,
        "plan": plan,
        "verification": v["result"],
        "response": r["output"],
        "trace": trace.to_list(),
        "trace_root_hash": trace.root_hash(),
    }
