"""
Graph Memory — NetworkX-based memory store.
Stores goals, entities, constraints, and their relations.
"""

import networkx as nx
from typing import Optional, Any
from datetime import datetime
import json


class GraphMemory:
    """
    Simple graph-based memory using NetworkX.
    Stores goals, entities, constraints and their relationships.
    """
    
    def __init__(self):
        self.graph = nx.DiGraph()
        self.snapshots: list[dict] = []  # For before/after comparison
    
    def snapshot(self) -> dict:
        """Take a snapshot of current state."""
        snapshot = {
            "timestamp": datetime.utcnow().isoformat(),
            "nodes": list(self.graph.nodes(data=True)),
            "edges": list(self.graph.edges(data=True)),
            "node_count": self.graph.number_of_nodes(),
            "edge_count": self.graph.number_of_edges()
        }
        self.snapshots.append(snapshot)
        return snapshot
    
    def add_goal(self, node_id: str, goal_text: str, goal_type: str):
        """Add a goal node."""
        self.graph.add_node(
            node_id,
            type="goal",
            text=goal_text,
            goal_type=goal_type,
            created_at=datetime.utcnow().isoformat(),
            status="active"
        )
    
    def add_entity(self, node_id: str, name: str, properties: dict = None):
        """Add an entity node."""
        self.graph.add_node(
            node_id,
            type="entity",
            name=name,
            properties=properties or {},
            created_at=datetime.utcnow().isoformat()
        )
    
    def add_constraint(self, node_id: str, constraint_type: str, key: str, value: Any):
        """Add a constraint node."""
        self.graph.add_node(
            node_id,
            type="constraint",
            constraint_type=constraint_type,
            key=key,
            value=value,
            created_at=datetime.utcnow().isoformat()
        )
    
    def add_relation(self, from_id: str, to_id: str, relation_type: str):
        """Add an edge between nodes."""
        self.graph.add_edge(
            from_id,
            to_id,
            type=relation_type,
            created_at=datetime.utcnow().isoformat()
        )
    
    def update_node(self, node_id: str, **updates):
        """Update node properties."""
        if node_id in self.graph.nodes:
            for key, value in updates.items():
                self.graph.nodes[node_id][key] = value
            self.graph.nodes[node_id]["updated_at"] = datetime.utcnow().isoformat()
    
    def get_node(self, node_id: str) -> Optional[dict]:
        """Get a node by ID."""
        if node_id in self.graph.nodes:
            return dict(self.graph.nodes[node_id])
        return None
    
    def get_related(self, node_id: str, relation_type: str = None) -> list[tuple]:
        """Get nodes related to a given node."""
        related = []
        
        # Outgoing edges
        for _, target, data in self.graph.out_edges(node_id, data=True):
            if relation_type is None or data.get("type") == relation_type:
                related.append((target, data.get("type"), self.get_node(target)))
        
        # Incoming edges
        for source, _, data in self.graph.in_edges(node_id, data=True):
            if relation_type is None or data.get("type") == relation_type:
                related.append((source, data.get("type"), self.get_node(source)))
        
        return related
    
    def find_goals(self, status: str = None) -> list[dict]:
        """Find all goal nodes."""
        goals = []
        for node_id, data in self.graph.nodes(data=True):
            if data.get("type") == "goal":
                if status is None or data.get("status") == status:
                    goals.append({"id": node_id, **data})
        return goals
    
    def get_context_for_goal(self, goal_id: str) -> dict:
        """Get full context for a goal (entities, constraints)."""
        if goal_id not in self.graph.nodes:
            return {}
        
        goal = self.get_node(goal_id)
        related = self.get_related(goal_id)
        
        entities = []
        constraints = []
        
        for node_id, rel_type, node_data in related:
            if node_data:
                if node_data.get("type") == "entity":
                    entities.append({"id": node_id, **node_data})
                elif node_data.get("type") == "constraint":
                    constraints.append({"id": node_id, **node_data})
        
        return {
            "goal": {"id": goal_id, **goal},
            "entities": entities,
            "constraints": constraints
        }
    
    def to_demo_json(self) -> dict:
        """Export graph for demo display."""
        nodes = []
        for node_id, data in self.graph.nodes(data=True):
            nodes.append({
                "id": node_id,
                "type": data.get("type", "unknown"),
                "label": data.get("text") or data.get("name") or data.get("key", node_id),
                "data": {k: v for k, v in data.items() if k not in ["type"]}
            })
        
        edges = []
        for source, target, data in self.graph.edges(data=True):
            edges.append({
                "source": source,
                "target": target,
                "type": data.get("type", "related")
            })
        
        return {
            "nodes": nodes,
            "edges": edges,
            "stats": {
                "node_count": len(nodes),
                "edge_count": len(edges)
            }
        }
    
    def clear(self):
        """Clear all memory."""
        self.graph.clear()
        self.snapshots = []


# Singleton instance
_memory_instance: Optional[GraphMemory] = None


def get_memory() -> GraphMemory:
    """Get the global memory instance."""
    global _memory_instance
    if _memory_instance is None:
        _memory_instance = GraphMemory()
    return _memory_instance


def reset_memory():
    """Reset the global memory instance."""
    global _memory_instance
    _memory_instance = GraphMemory()
    return _memory_instance
