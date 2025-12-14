"""Base agent class for Harmonia cognitive kernel."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class AgentStatus(str, Enum):
    SUCCESS = "success"
    PARTIAL = "partial"
    CONFLICT = "conflict"
    UNCERTAIN = "uncertain"
    ERROR = "error"


@dataclass
class AgentResult:
    """Result from an agent execution."""

    agent_name: str
    status: AgentStatus
    output: Any
    confidence: float = 1.0
    reasoning: str = ""
    conflicts: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "agent": self.agent_name,
            "status": self.status.value,
            "confidence": self.confidence,
            "reasoning": self.reasoning,
            "conflicts": self.conflicts,
            "output": self.output if isinstance(self.output, (dict, list, str, int, float, bool, type(None))) else str(self.output),
            "metadata": self.metadata,
        }


class BaseAgent(ABC):
    """Abstract base class for all Harmonia agents."""

    name: str = "BaseAgent"
    description: str = "Base agent"

    def __init__(self, llm_provider=None):
        self.llm = llm_provider

    @abstractmethod
    async def execute(self, input_data: Any, context: dict[str, Any] = None) -> AgentResult:
        """Execute the agent's primary function."""
        pass

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"
