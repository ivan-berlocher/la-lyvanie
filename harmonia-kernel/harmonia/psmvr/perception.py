from __future__ import annotations
from dataclasses import dataclass
from typing import Literal, Dict, Any
import datetime

@dataclass(frozen=True)
class PerceptionOutput:
    text: str
    modality: Literal["text"] = "text"
    timestamp: str = ""

def perceive(raw_text: str) -> Dict[str, Any]:
    text = " ".join(raw_text.strip().split())
    ts = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="milliseconds").replace("+00:00","Z")
    return {"text": text, "modality": "text", "timestamp": ts}
