"""
Trace Logger — Execution logging for transparency.
Every step is logged with input, output, agent, and latency.
"""

from pydantic import BaseModel
from typing import Any, Optional
from datetime import datetime
from uuid import uuid4
import json


class TraceEntry(BaseModel):
    """Single trace entry for one pipeline step."""
    trace_id: str
    request_id: str
    step: str  # perception, sensemaking, modeling, response
    input_summary: str
    output_summary: str
    agent: Optional[str] = None
    model: Optional[str] = None
    latency_ms: int
    timestamp: datetime = None
    metadata: dict = {}
    
    def __init__(self, **data):
        super().__init__(**data)
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()


class RequestTrace(BaseModel):
    """Complete trace for one request."""
    request_id: str
    user_input: str
    entries: list[TraceEntry] = []
    total_latency_ms: int = 0
    success: bool = True
    model_used: str = "unknown"
    timestamp: datetime = None
    
    def __init__(self, **data):
        super().__init__(**data)
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()
    
    def to_demo_json(self) -> dict:
        """Return clean JSON for demo display."""
        return {
            "request_id": self.request_id[:8] + "...",
            "input": self.user_input[:100] + ("..." if len(self.user_input) > 100 else ""),
            "model": self.model_used,
            "total_latency_ms": self.total_latency_ms,
            "success": self.success,
            "steps": [
                {
                    "step": e.step,
                    "agent": e.agent,
                    "latency_ms": e.latency_ms,
                    "output": e.output_summary[:200]
                }
                for e in self.entries
            ]
        }


class TraceLogger:
    """
    Logs all pipeline execution for transparency.
    This is the "Thinking Panel" data source.
    """
    
    def __init__(self):
        self.traces: dict[str, RequestTrace] = {}
        self.current_request_id: Optional[str] = None
        self._simple_entries: list[dict] = []  # Simple log for demo UI
    
    def clear(self):
        """Clear current simple entries for new request."""
        self._simple_entries = []
    
    def log(self, phase: str, event: str, data: Any = None):
        """Simple log method for demo UI."""
        self._simple_entries.append({
            "phase": phase,
            "event": event,
            "data": data or {},
            "timestamp": datetime.utcnow().strftime("%H:%M:%S.%f")[:-3]
        })
    
    def get_entries(self) -> list[dict]:
        """Get simple entries for demo UI."""
        return self._simple_entries
    
    def start_request(self, user_input: str, model: str = "unknown") -> str:
        """Start tracing a new request."""
        request_id = str(uuid4())
        self.current_request_id = request_id
        
        self.traces[request_id] = RequestTrace(
            request_id=request_id,
            user_input=user_input,
            model_used=model
        )
        
        return request_id
    
    def log_step(
        self,
        step: str,
        input_data: Any,
        output_data: Any,
        latency_ms: int,
        agent: Optional[str] = None,
        model: Optional[str] = None,
        metadata: dict = {}
    ):
        """Log a pipeline step."""
        if not self.current_request_id:
            return
        
        trace = self.traces[self.current_request_id]
        
        # Summarize input/output
        input_summary = self._summarize(input_data)
        output_summary = self._summarize(output_data)
        
        entry = TraceEntry(
            trace_id=str(uuid4()),
            request_id=self.current_request_id,
            step=step,
            input_summary=input_summary,
            output_summary=output_summary,
            agent=agent,
            model=model,
            latency_ms=latency_ms,
            metadata=metadata
        )
        
        trace.entries.append(entry)
        trace.total_latency_ms += latency_ms
        
        if model:
            trace.model_used = model
    
    def end_request(self, success: bool = True) -> RequestTrace:
        """End the current request trace."""
        if not self.current_request_id:
            return None
        
        trace = self.traces[self.current_request_id]
        trace.success = success
        
        request_id = self.current_request_id
        self.current_request_id = None
        
        return trace
    
    def get_trace(self, request_id: str) -> Optional[RequestTrace]:
        """Get a specific trace."""
        return self.traces.get(request_id)
    
    def get_recent_traces(self, limit: int = 10) -> list[RequestTrace]:
        """Get recent traces for demo display."""
        traces = list(self.traces.values())
        traces.sort(key=lambda t: t.timestamp, reverse=True)
        return traces[:limit]
    
    def _summarize(self, data: Any, max_len: int = 500) -> str:
        """Summarize data for logging."""
        if data is None:
            return "null"
        
        if hasattr(data, "model_dump"):
            # Pydantic model
            text = json.dumps(data.model_dump(), default=str)
        elif isinstance(data, dict):
            text = json.dumps(data, default=str)
        elif isinstance(data, str):
            text = data
        else:
            text = str(data)
        
        if len(text) > max_len:
            return text[:max_len] + "..."
        return text
    
    def export_logs(self, filepath: str):
        """Export all traces to JSON file."""
        data = {
            request_id: trace.model_dump()
            for request_id, trace in self.traces.items()
        }
        
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2, default=str)
