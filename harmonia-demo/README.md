# Harmonia Demo — MVP

Cognitive kernel demonstration for PhD contact.

## Core Invariant

> **For a given input, the UIL schema and verification rules remain identical across models.**

Same kernel, same UIL schema, same verifier. Only the parser and planner swap their underlying model.

## Quick Start

```bash
cd harmonia-demo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open: http://localhost:8000

## Architecture

```
Input (text)
     ↓
UIL (typed intent)
     ↓
Graph Memory + Goal
     ↓
Agent Routing
     ↓
Action
     ↓
Trace
```

## Design Decisions

| Component | LLM? | Rationale |
|-----------|------|-----------|
| IntentParser | ✅ | Strict JSON schema via OpenAI Structured Outputs |
| Planner | ✅ | Strict JSON schema, deterministic (temp=0, seed=42) |
| Perception | ❌ | Kernel-driven, no model dependency |
| **Verifier** | ❌ | **Non-LLM by design: preserves auditability and trust** |
| Memory | ❌ | Deterministic graph (NetworkX) |
| Trace | ❌ | Pure logging, immutable |

## Components

| Component | File | Purpose |
|-----------|------|---------|
| UIL Schema | `uil/schema.py` | Typed intent representation |
| PSMR Pipeline | `psmr/` | Perception → Sensemaking → Modeling → Response |
| Graph Memory | `memory/graph.py` | NetworkX-based memory |
| Agents | `agents/` | IntentParser, Planner, Verifier |
| Trace | `psmr/trace.py` | Execution logs |
| API | `main.py` | FastAPI endpoints |
| UI | `static/index.html` | Single-page demo interface |

## Demo Strategy (PhD)

```
1st run: Mock     → Architecture, trace, kernel visible
2nd run: GPT-4o-mini → Interchangeability, same invariants
3rd run: Local (opt) → Sovereignty, provider independence
```

## Demo Scenarios

1. **Simple plan:** "Plan a 3-day trip in Zurich next month"
2. **Modify goal:** "Reduce the budget by 20%"
3. **Model switch:** Same query, different LLM
4. **Failure case:** Trigger uncertainty / conflict

## Success Criteria

The demo succeeds if the professor says:

- "This is not just prompting."
- "I can see the intermediate representation."
- "This could be formalized and evaluated."
