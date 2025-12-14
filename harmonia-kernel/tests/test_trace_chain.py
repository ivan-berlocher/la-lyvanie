from harmonia.psmvr.kernel import run

def test_trace_chain():
    out = run("Plan a 3-day trip to Zurich next month under 500 CHF")
    trace = out["trace"]
    # prev_hash should equal previous output_hash
    prev = None
    for ev in trace:
        assert ev["prev_hash"] == prev
        prev = ev["output_hash"]
