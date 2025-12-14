# Harmonia Kernel (PSMVR) — Reference Implementation (v1.0.0)

This repository provides a minimal, reproducible implementation of the Harmonia cognitive kernel described in the white paper:

> **Harmonia: A Verifiable Cognitive Kernel for Presence-Oriented AI Systems**

**PSMVR**: Perception → Sensemaking → Modeling → Verification → Response

The implementation is designed to demonstrate the core architectural invariants:

- **Typed cognitive IR**: Universal Intent Language (UIL)
- **Typed execution IR**: Plan Intermediate Representation (PIR)
- **Non-LLM deterministic verification**
- **Trace completeness** with canonical hashing and replay-friendly artifacts
- **Model interchangeability at the boundary** (semantic parsing is replaceable; kernel logic is invariant)

---

## Core Invariant

Once intent is extracted into **UIL**, all downstream reasoning, verification, and execution are **deterministic** and **model-invariant**. The verifier depends only on **UIL + PIR + memory state**, not on LLM inference.

---

## Installation

**Requirements:** Python 3.11+

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

---

## Quick Demo (deterministic, no API keys)

```bash
harmonia-demo --input "Plan a 3-day trip to Zurich next month under 500 CHF" --mode mock --outdir out
```

This writes:

| File | Description |
|------|-------------|
| `out/uil.json` | Extracted UIL (typed intent IR) |
| `out/plan.json` | Proposed PIR (typed plan IR) |
| `out/verification.json` | Verification result (deterministic) |
| `out/response.json` | Response payload |
| `out/trace.json` | Full PSMVR trace (hash-chained) |
| `out/trace_root_hash.txt` | SHA-256 hash of the complete trace |

---

## Demo Protocol (Paper Alignment)

Run the scripted protocol:

```bash
bash demo_protocol.sh
```

### Protocol Structure

| Run | Mode | Purpose |
|-----|------|---------|
| **Run 1** | `mock` | Baseline — produces artifacts + trace |
| **Run 2** | `mock` | Replay — validates verifier determinism and trace replayability |
| **Run 3** | `gpt` (optional) | LLM parser — demonstrates model interchangeability (placeholder) |

**Run 3 Note:** This step is included as a placeholder for a future `--mode gpt` implementation. Once enabled, it demonstrates that different semantic front-ends can produce equivalent UIL under controlled extraction, while verification remains invariant given equivalent UIL.

---

## How to Verify the Trace Chain

Each event in `trace.json` includes:

| Field | Description |
|-------|-------------|
| `input_hash` | SHA-256 of canonical serialized input |
| `output_hash` | SHA-256 of canonical serialized output |
| `prev_hash` | Previous event's `output_hash` (hash chain) |

### Canonical Hashing Rule

Hashes are computed over canonical JSON:

- UTF-8 encoding
- Stable key ordering (sorted keys)
- No extraneous whitespace (compact separators: `separators=(',', ':')`)

This ensures **cross-implementation reproducibility**.

---

## Project Structure

```
harmonia-kernel/
├── harmonia/
│   ├── __init__.py
│   ├── demo/
│   │   └── cli.py              # CLI entry point
│   ├── pir/
│   │   └── schema.py           # Plan Intermediate Representation
│   ├── psmvr/
│   │   ├── kernel.py           # PSMVR orchestrator
│   │   ├── perception.py       # P stage
│   │   ├── sensemaking.py      # S stage (LLM boundary)
│   │   ├── modeling.py         # M stage
│   │   ├── verification.py     # V stage (non-LLM, deterministic)
│   │   ├── response.py         # R stage
│   │   └── trace.py            # Trace + canonical hashing
│   └── uil/
│       ├── schema.py           # Universal Intent Language
│       └── equivalence.py      # UIL structural equivalence
├── examples/
│   └── inputs/
│       └── trip.txt            # Example input
├── tests/
│   ├── test_trace_chain.py     # Trace hash chain validation
│   └── test_verifier_determinism.py  # Verifier invariance test
├── demo_protocol.sh            # Paper-aligned demo script
├── pyproject.toml
├── LICENSE
└── CITATION.cff
```

---

## Running Tests

```bash
pytest tests/ -v
```

**Test coverage:**

- `test_trace_chain.py` — Validates hash chain integrity (`prev_hash` links)
- `test_verifier_determinism.py` — Confirms verifier produces identical results for identical UIL

---

## Citation

See `CITATION.cff` for citation metadata.

```bibtex
@software{harmonia_kernel,
  author = {Harmonia},
  title = {Harmonia Kernel: A Verifiable Cognitive Kernel for Presence-Oriented AI Systems},
  year = {2025},
  url = {https://github.com/harmonia-project/harmonia-kernel}
}
```

---

## Scope / Non-Goals

This MVP focuses on **kernel invariants**. It does **not** include:

- Tool execution connectors (calendar, email, etc.)
- External world validation (availability, real pricing, etc.)
- Adversarial defenses beyond anomaly surfacing
- Production-grade error handling

---

## License

MIT (see `LICENSE`)

---

*Harmonia is an open research initiative developing verifiable cognitive architectures grounded in presence and non-directive interaction.*

MIT
