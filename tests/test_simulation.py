from app.services.simulation_engine import SimulationState

def test_run_basic():
    graph = {"nodes":[{"id":"n0","text":"현실 테스트", "confidence":0.5, "importance":0.5}],
             "edges":[]}
    value_vector = {"realism":0.8,"simplicity":0.6}
    rules = {"forbidden":["금지어"]}
    st = SimulationState(graph, value_vector, rules)
    events, snap = st.run(steps=3)
    assert len(events) == 3
    assert snap["graph"]["nodes"][0]["importance"] >= 0.5
