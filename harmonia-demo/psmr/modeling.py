"""
Modeling Step — Memory update + Agent routing
Updates graph memory and routes to appropriate agents.
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from uil import Intent
from .sensemaking import SensemakingOutput


class AgentDecision(BaseModel):
    """Result from an agent."""
    agent_name: str
    decision: str
    confidence: float
    notes: str
    timestamp: datetime = None
    
    def __init__(self, **data):
        super().__init__(**data)
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()


class ModelingOutput(BaseModel):
    """Output of modeling: memory updates + agent decisions."""
    intent: Intent
    memory_updates: list[dict]
    agent_decisions: list[AgentDecision]
    selected_action: str
    conflict_detected: bool = False
    uncertainty_flag: bool = False


class ModelingStep:
    """
    M in PSMR — Modeling
    Updates world model (graph memory) and routes to agents.
    """
    
    def __init__(self, memory_graph, agents: list):
        self.memory = memory_graph
        self.agents = {a.name: a for a in agents}
    
    async def process(
        self,
        sensemaking: SensemakingOutput,
        llm_client
    ) -> ModelingOutput:
        """Update memory and get agent decisions."""
        
        intent = sensemaking.intent
        memory_updates = []
        agent_decisions = []
        
        # 1. Update graph memory
        memory_updates = self._update_memory(intent)
        
        # 2. Route to agents based on intent type
        relevant_agents = self._select_agents(intent)
        
        # 3. Get decisions from each agent
        for agent_name in relevant_agents:
            if agent_name in self.agents:
                agent = self.agents[agent_name]
                decision = await agent.process(intent, self.memory, llm_client)
                agent_decisions.append(decision)
        
        # 4. Check for conflicts
        conflict_detected = self._detect_conflicts(agent_decisions)
        uncertainty_flag = intent.confidence < 0.5 or any(d.confidence < 0.5 for d in agent_decisions)
        
        # 5. Select action (or flag for review)
        if conflict_detected:
            selected_action = "CONFLICT_DETECTED: Manual review required"
        elif uncertainty_flag:
            selected_action = "UNCERTAINTY: Clarification needed"
        else:
            selected_action = self._select_best_action(agent_decisions)
        
        return ModelingOutput(
            intent=intent,
            memory_updates=memory_updates,
            agent_decisions=agent_decisions,
            selected_action=selected_action,
            conflict_detected=conflict_detected,
            uncertainty_flag=uncertainty_flag
        )
    
    def _update_memory(self, intent: Intent) -> list[dict]:
        """Update graph memory with intent information."""
        updates = []
        
        # Add goal node
        goal_id = f"goal:{intent.intent_id[:8]}"
        self.memory.add_goal(goal_id, intent.goal, intent.type)
        updates.append({"action": "add_node", "type": "goal", "id": goal_id})
        
        # Add entity nodes
        for entity in intent.entities:
            entity_id = f"entity:{entity.lower().replace(' ', '_')}"
            self.memory.add_entity(entity_id, entity)
            self.memory.add_relation(goal_id, entity_id, "involves")
            updates.append({"action": "add_node", "type": "entity", "id": entity_id})
        
        # Add constraint nodes
        for constraint in intent.constraints:
            constraint_id = f"constraint:{constraint.type}_{constraint.key}"
            self.memory.add_constraint(constraint_id, constraint.type, constraint.key, constraint.value)
            self.memory.add_relation(goal_id, constraint_id, "has_constraint")
            updates.append({"action": "add_node", "type": "constraint", "id": constraint_id})
        
        return updates
    
    def _select_agents(self, intent: Intent) -> list[str]:
        """Select which agents should process this intent."""
        agents = ["IntentParser"]  # Always verify parsing
        
        if intent.type == "PLAN":
            agents.append("Planner")
        elif intent.type == "ACTION":
            agents.append("Planner")
        elif intent.type == "QUERY":
            agents.append("Planner")
        
        # Always add verifier
        agents.append("Verifier")
        
        return agents
    
    def _detect_conflicts(self, decisions: list[AgentDecision]) -> bool:
        """Check if agents have conflicting decisions."""
        if len(decisions) < 2:
            return False
        
        # Simple conflict detection: very different confidence levels
        confidences = [d.confidence for d in decisions]
        if max(confidences) - min(confidences) > 0.4:
            return True
        
        return False
    
    def _select_best_action(self, decisions: list[AgentDecision]) -> str:
        """Select the best action from agent decisions."""
        if not decisions:
            return "No action determined"
        
        # Select highest confidence decision
        best = max(decisions, key=lambda d: d.confidence)
        return best.decision
