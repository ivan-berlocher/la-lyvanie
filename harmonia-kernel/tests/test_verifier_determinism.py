from harmonia.psmvr.kernel import run

def test_determinism_mock():
    a = run("Plan a 3-day trip to Zurich next month under 500 CHF")
    b = run("Plan a 3-day trip to Zurich next month under 500 CHF")
    # root hash may differ because timestamps differ; compare verification outcomes
    assert a["verification"]["valid"] == b["verification"]["valid"]
    assert a["verification"]["approval_required"] == b["verification"]["approval_required"]
