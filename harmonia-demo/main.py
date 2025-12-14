"""
Harmonia Cognitive Kernel - Demo Server

A demonstration of the PSMR pipeline and multi-agent architecture
for PhD presentations. Shows traceable, structured AI reasoning.

Run with: uvicorn main:app --reload
"""

import asyncio
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from agents import IntentParserAgent, PlannerAgent, VerifierAgent
from llm import get_provider, switch_model
from llm.provider import get_available_models
from memory import get_memory, reset_memory
from psmr import PerceptionStep, SensemakingStep, ModelingStep, ResponseStep
from psmr.trace import TraceLogger

# Initialize FastAPI app
app = FastAPI(
    title="Harmonia Cognitive Kernel",
    description="PSMR Pipeline Demo for PhD Research",
    version="0.1.0",
)

# CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request/Response models
class RunRequest(BaseModel):
    input: str
    include_trace: bool = True
    include_memory: bool = True


class RunResponse(BaseModel):
    success: bool
    intent: Optional[dict] = None
    plan: Optional[dict] = None
    verification: Optional[dict] = None
    response: Optional[str] = None
    trace: Optional[list] = None
    memory_before: Optional[dict] = None
    memory_after: Optional[dict] = None
    model_used: str = "unknown"
    latency_ms: float = 0.0
    used_fallback: bool = False  # True if LLM failed and fell back to mock


class SwitchModelRequest(BaseModel):
    provider: str  # "openai", "mock", "local"
    model: Optional[str] = None


class StatusResponse(BaseModel):
    status: str
    current_provider: str
    current_model: str
    memory_nodes: int
    memory_edges: int


# Global trace logger
trace_logger = TraceLogger()


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main UI."""
    static_path = Path(__file__).parent / "static" / "index.html"
    if static_path.exists():
        return HTMLResponse(content=static_path.read_text())
    return HTMLResponse(content="""
    <html>
        <head><title>Harmonia Demo</title></head>
        <body>
            <h1>Harmonia Cognitive Kernel</h1>
            <p>Static files not found. Use the API directly:</p>
            <ul>
                <li>POST /run - Run PSMR pipeline</li>
                <li>POST /switch - Switch LLM model</li>
                <li>GET /status - Get system status</li>
                <li>POST /reset - Reset memory</li>
            </ul>
        </body>
    </html>
    """)


@app.get("/status", response_model=StatusResponse)
async def get_status():
    """Get current system status."""
    provider = get_provider()
    memory = get_memory()
    snapshot = memory.get_snapshot()

    return StatusResponse(
        status="running",
        current_provider=provider.name,
        current_model=provider.current_model,
        memory_nodes=snapshot.get("node_count", 0),
        memory_edges=snapshot.get("edge_count", 0),
    )


@app.get("/models")
async def list_models():
    """List available models."""
    return get_available_models()


@app.post("/switch")
async def switch_llm(request: SwitchModelRequest):
    """Switch LLM provider/model."""
    try:
        provider = switch_model(request.provider, request.model)
        return {
            "success": True,
            "provider": provider.name,
            "model": provider.current_model,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to switch model: {str(e)}")


@app.post("/reset")
async def reset():
    """Reset memory graph."""
    reset_memory()
    trace_logger.clear()
    return {"success": True, "message": "Memory and trace cleared"}


@app.post("/run", response_model=RunResponse)
async def run_pipeline(request: RunRequest):
    """
    Execute the full PSMR pipeline.
    
    This is the main demo endpoint showing:
    1. Structured intent parsing (not just prompting)
    2. Multi-agent planning
    3. Verification with conflict detection
    4. Traceable execution
    5. Memory graph updates
    """
    start_time = datetime.now()
    trace_logger.clear()
    
    provider = get_provider()
    memory = get_memory()

    # Capture memory before
    memory_before = memory.snapshot() if request.include_memory else None

    try:
        # ====== PERCEPTION ======
        trace_logger.log("perception", "start", {"input_length": len(request.input)})
        perception = PerceptionStep()
        perception_result = await perception.process(request.input)
        trace_logger.log("perception", "complete", {"result": perception_result.to_dict()})

        # ====== SENSEMAKING (Intent Parsing) ======
        trace_logger.log("sensemaking", "start", {"agent": "IntentParser"})
        parser = IntentParserAgent(llm_provider=provider)
        intent_result = await parser.execute(perception_result.normalized_text)
        trace_logger.log("sensemaking", "complete", intent_result.to_dict())

        if intent_result.status.value == "error":
            raise ValueError(f"Intent parsing failed: {intent_result.reasoning}")

        intent = intent_result.output

        # Update memory with intent
        memory.add_goal(intent.get("intent_id", "unknown"), intent.get("goal", ""), intent.get("type", "ACTION"))
        for entity in intent.get("entities", []):
            memory.add_entity(entity, entity)
            memory.add_relation(intent.get("intent_id", "unknown"), entity, "references")

        # ====== MODELING (Planning) ======
        trace_logger.log("modeling", "start", {"agent": "Planner"})
        planner = PlannerAgent(llm_provider=provider)
        plan_result = await planner.execute(
            intent,
            context={"memory_snapshot": memory.snapshot()},
        )
        trace_logger.log("modeling", "complete", plan_result.to_dict())

        plan = plan_result.output if plan_result.output else {}

        # ====== VERIFICATION ======
        trace_logger.log("verification", "start", {"agent": "Verifier"})
        verifier = VerifierAgent(llm_provider=provider)
        verification_result = await verifier.execute(
            {"intent": intent, "plan": plan},
            context={"memory_snapshot": memory.snapshot()},
        )
        trace_logger.log("verification", "complete", verification_result.to_dict())

        # ====== RESPONSE GENERATION ======
        trace_logger.log("response", "start", {})
        response_step = ResponseStep()
        final_response = await response_step.generate(
            intent=intent,
            plan=plan,
            verification=verification_result.output,
        )
        trace_logger.log("response", "complete", {"response_length": len(final_response)})

        # Update memory with plan
        if plan.get("plan_id"):
            memory.add_goal(plan["plan_id"], f"Plan: {len(plan.get('steps', []))} steps", "PLAN")
            memory.add_relation(intent.get("intent_id", "unknown"), plan["plan_id"], "generated")

        # Capture memory after
        memory_after = memory.snapshot() if request.include_memory else None

        # Calculate latency
        latency_ms = (datetime.now() - start_time).total_seconds() * 1000

        # Check if any agent used fallback
        used_fallback = (
            intent_result.metadata.get("used_fallback", False) or
            plan_result.metadata.get("used_fallback", False)
        )

        return RunResponse(
            success=True,
            intent=intent,
            plan=plan,
            verification=verification_result.output,
            response=final_response,
            trace=trace_logger.get_entries() if request.include_trace else None,
            memory_before=memory_before,
            memory_after=memory_after,
            model_used=provider.current_model,
            latency_ms=latency_ms,
            used_fallback=used_fallback,
        )

    except Exception as e:
        trace_logger.log("error", "pipeline_failed", {"error": str(e)})
        latency_ms = (datetime.now() - start_time).total_seconds() * 1000

        return RunResponse(
            success=False,
            response=f"Pipeline error: {str(e)}",
            trace=trace_logger.get_entries() if request.include_trace else None,
            memory_before=memory_before,
            memory_after=memory.snapshot() if request.include_memory else None,
            model_used=provider.current_model,
            latency_ms=latency_ms,
        )


@app.get("/trace")
async def get_trace():
    """Get current trace log."""
    return {"trace": trace_logger.get_entries()}


@app.get("/memory")
async def get_memory_state():
    """Get current memory graph state."""
    memory = get_memory()
    return memory.to_dict()


# Mount static files if directory exists
static_dir = Path(__file__).parent / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
    )
