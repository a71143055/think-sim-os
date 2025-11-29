import networkx as nx
from typing import Dict, List

def build_graph_from_chat(chat_items: List[Dict], value_vector: Dict) -> nx.DiGraph:
    G = nx.DiGraph()
    node_id = 0
    for item in chat_items:
        # 문장 단위로 노드화
        sentences = [s.strip() for s in item["text"].replace("\n", " ").split(".") if s.strip()]
        for s in sentences:
            nid = f"n{node_id}"
            G.add_node(nid, text=s, role=item["role"], confidence=0.5, importance=0.5)
            node_id += 1

    # 순차 엣지
    nodes = list(G.nodes())
    for i in range(len(nodes) - 1):
        G.add_edge(nodes[i], nodes[i+1], relation="sequence", weight=1.0)

    # 현실성 키워드 영향
    realism_keywords = {"현실", "실제", "데이터", "증거", "테스트"}
    for nid, data in G.nodes(data=True):
        words = set(data["text"].split())
        if len(words & realism_keywords) > 0:
            data["confidence"] = min(1.0, data["confidence"] + value_vector.get("realism", 0.0) * 0.3)
    return G

def serialize_graph(G: nx.DiGraph) -> dict:
    return {
        "nodes": [{"id": n, **d} for n, d in G.nodes(data=True)],
        "edges": [{"src": u, "dst": v, **d} for u, v, d in G.edges(data=True)]
    }
