#!/usr/bin/env bash
# demo_protocol.sh — Paper-aligned demonstration protocol for Harmonia Kernel
# 
# This script executes the demo protocol described in the whitepaper:
#   Run 1: mock baseline
#   Run 2: mock replay (determinism check)
#   Run 3: gpt mode (optional, placeholder)
#
# Usage: bash demo_protocol.sh

set -euo pipefail

INPUT='Plan a 3-day trip to Zurich next month under 500 CHF'

echo "=============================================="
echo "  Harmonia Kernel — Demo Protocol"
echo "=============================================="
echo ""
echo "Input: \"$INPUT\""
echo ""

# Clean previous runs
rm -rf out_run1 out_run2 out_run_gpt 2>/dev/null || true

# ─────────────────────────────────────────────────
# Run 1: Mock baseline
# ─────────────────────────────────────────────────
echo "[Run 1] mock baseline"
harmonia-demo --input "$INPUT" --mode mock --outdir out_run1 >/dev/null
HASH1=$(cat out_run1/trace_root_hash.txt)
echo "  ✓ trace_root_hash: $HASH1"
echo ""

# ─────────────────────────────────────────────────
# Run 2: Mock replay (determinism check)
# ─────────────────────────────────────────────────
echo "[Run 2] mock replay (determinism check)"
harmonia-demo --input "$INPUT" --mode mock --outdir out_run2 >/dev/null
HASH2=$(cat out_run2/trace_root_hash.txt)
echo "  ✓ trace_root_hash: $HASH2"
echo ""

# ─────────────────────────────────────────────────
# Check: Verification invariance
# ─────────────────────────────────────────────────
echo "[Check] Verification invariance (Run 1 vs Run 2)"
python3 - <<'PY'
import json
import sys

v1 = json.load(open('out_run1/verification.json'))
v2 = json.load(open('out_run2/verification.json'))

same_valid = v1.get("valid") == v2.get("valid")
same_approval = v1.get("approval_required") == v2.get("approval_required")
invariant = same_valid and same_approval

if invariant:
    print("  ✓ verifier_invariance: PASS")
    print(f"    valid={v1.get('valid')}, approval_required={v1.get('approval_required')}")
else:
    print("  ✗ verifier_invariance: FAIL")
    print(f"    Run 1: valid={v1.get('valid')}, approval_required={v1.get('approval_required')}")
    print(f"    Run 2: valid={v2.get('valid')}, approval_required={v2.get('approval_required')}")
    sys.exit(1)
PY
echo ""

# ─────────────────────────────────────────────────
# Check: Trace hash equality (determinism)
# ─────────────────────────────────────────────────
echo "[Check] Trace hash equality (determinism)"
if [ "$HASH1" = "$HASH2" ]; then
    echo "  ✓ trace_hash_equality: PASS"
    echo "    Both runs produced identical trace_root_hash"
else
    echo "  ✗ trace_hash_equality: FAIL"
    echo "    Run 1: $HASH1"
    echo "    Run 2: $HASH2"
fi
echo ""

# ─────────────────────────────────────────────────
# Run 3: GPT mode (placeholder)
# ─────────────────────────────────────────────────
echo "[Run 3] LLM parser mode (placeholder)"
echo "  NOTE: This repo currently supports only --mode mock."
echo "  To enable Run 3, implement --mode gpt in:"
echo "    - harmonia/psmvr/sensemaking.py"
echo "    - harmonia/demo/cli.py"
echo ""
echo "  Once enabled, Run 3 will demonstrate that different semantic"
echo "  front-ends can produce equivalent UIL, while verification"
echo "  remains invariant given equivalent UIL."
echo ""

# ─────────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────────
echo "=============================================="
echo "  Demo Protocol — Summary"
echo "=============================================="
echo ""
echo "Success criteria (from whitepaper Section 9.2):"
echo "  (a) Identical verification outcomes for equivalent UIL across runs"
echo "  (b) Guaranteed rejection of constraint-violating plans"
echo ""
echo "Artifacts produced:"
echo "  out_run1/  — baseline artifacts"
echo "  out_run2/  — replay artifacts"
echo ""
echo "To inspect the trace chain:"
echo "  cat out_run1/trace.json | python -m json.tool"
echo ""
echo "To verify hash chain integrity:"
echo "  pytest tests/test_trace_chain.py -v"
echo ""
