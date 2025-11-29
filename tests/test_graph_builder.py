from app.services.graph_builder import build_graph_from_chat, serialize_graph

def test_build_graph():
    chat = [{"role":"user","text":"현실적 이미지 트레이닝을 한다. 데이터로만 보지 말자."}]
    g = build_graph_from_chat(chat, {"realism":0.7})
    js = serialize_graph(g)
    assert len(js["nodes"]) >= 2
    assert len(js["edges"]) >= 1
