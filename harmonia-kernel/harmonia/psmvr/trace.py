from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any, Literal, Optional, Dict
import hashlib, json, uuid, datetime

Step = Literal["P","S","M","V","R"]
Decision = Literal["accepted","rejected","approval_required","processed"]

def _canonical_json(obj: Any) -> str:
    # Stable key order, no whitespace, UTF-8 later
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha256_canonical(obj: Any) -> str:
    s = _canonical_json(obj).encode("utf-8")
    return hashlib.sha256(s).hexdigest()

@dataclass(frozen=True)
class TraceEvent:
    event_id: str
    trace_id: str
    step: Step
    timestamp: str
    input_hash: str
    output_hash: str
    prev_hash: Optional[str]
    decision: Decision
    duration_ms: int
    provenance: Dict[str, Any]
    links: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = None

def now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="milliseconds").replace("+00:00","Z")

def new_uuid() -> str:
    return str(uuid.uuid4())

class Trace:
    def __init__(self) -> None:
        self.trace_id = new_uuid()
        self.events: list[TraceEvent] = []
        self._prev: Optional[str] = None

    def append(self, step: Step, inp: Any, out: Any, decision: Decision, duration_ms: int,
               provenance: Dict[str, Any], links: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> TraceEvent:
        in_hash = sha256_canonical(inp)
        out_hash = sha256_canonical(out)
        ev = TraceEvent(
            event_id=new_uuid(),
            trace_id=self.trace_id,
            step=step,
            timestamp=now_iso(),
            input_hash=in_hash,
            output_hash=out_hash,
            prev_hash=self._prev,
            decision=decision,
            duration_ms=duration_ms,
            provenance=provenance,
            links=links,
            metadata=metadata,
        )
        self.events.append(ev)
        self._prev = out_hash
        return ev

    def to_list(self) -> list[dict[str, Any]]:
        return [asdict(e) for e in self.events]

    def root_hash(self) -> str:
        # hash of the whole trace (canonical)
        return sha256_canonical(self.to_list())
