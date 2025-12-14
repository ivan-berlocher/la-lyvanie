from __future__ import annotations
import argparse, json, os
from ..psmvr.kernel import run

def main() -> None:
    ap = argparse.ArgumentParser(description="Run Harmonia kernel demo (PSMVR) and emit artifacts.")
    ap.add_argument("--input", required=True, help="Input text")
    ap.add_argument("--mode", default="mock", choices=["mock"], help="Mode (mock deterministic)")
    ap.add_argument("--outdir", default="out", help="Output directory")
    args = ap.parse_args()

    out = run(args.input, mode=args.mode, model_name=args.mode)
    os.makedirs(args.outdir, exist_ok=True)
    for name in ["uil","plan","verification","response","trace"]:
        with open(os.path.join(args.outdir, f"{name}.json"), "w", encoding="utf-8") as f:
            json.dump(out[name], f, ensure_ascii=False, indent=2, sort_keys=True)
    with open(os.path.join(args.outdir, "trace_root_hash.txt"), "w", encoding="utf-8") as f:
        f.write(out["trace_root_hash"] + "\n")
    print(out["response"]["message"])
    print("\nTrace root hash:", out["trace_root_hash"])

if __name__ == "__main__":
    main()
