"""
Perception Step — Input processing
Receives raw input (text/voice), normalizes it.
"""

from pydantic import BaseModel
from typing import Literal
from datetime import datetime


class PerceptionInput(BaseModel):
    """Raw input from user."""
    content: str
    modality: Literal["text", "voice", "ui_event"] = "text"
    timestamp: datetime = None
    
    def __init__(self, **data):
        super().__init__(**data)
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()


class PerceptionOutput(BaseModel):
    """Normalized perception output."""
    raw_content: str
    normalized_content: str
    normalized_text: str  # Alias for normalized_content
    modality: str
    tokens: list[str]
    timestamp: datetime
    
    def to_dict(self) -> dict:
        return {
            "raw": self.raw_content[:100],
            "normalized": self.normalized_content[:100],
            "tokens": len(self.tokens),
            "modality": self.modality
        }


class PerceptionStep:
    """
    P in PSMR — Perception
    Normalizes and tokenizes input.
    """
    
    async def process(self, input_data: str | PerceptionInput) -> PerceptionOutput:
        """Process raw input into normalized form."""
        
        # Handle both string and PerceptionInput
        if isinstance(input_data, str):
            content = input_data
            modality = "text"
            timestamp = datetime.utcnow()
        else:
            content = input_data.content
            modality = input_data.modality
            timestamp = input_data.timestamp
        
        # Simple normalization
        normalized = content.strip()
        
        # Basic tokenization (for demo)
        tokens = normalized.split()
        
        return PerceptionOutput(
            raw_content=content,
            normalized_content=normalized,
            normalized_text=normalized,  # Alias
            modality=modality,
            tokens=tokens,
            timestamp=timestamp
        )
