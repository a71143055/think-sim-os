from typing import Dict, List, Tuple

class SimulationState:
    def __init__(self, graph: Dict, value_vector: Dict, rules: Dict):
        self.graph = graph
        self.value_vector = value_vector
        self.rules = rules
        self.time = 0
        self.log: List[Dict] = []
        self.focus = "explore"  # explore|converge|execute

    def step(self) -> Dict:
        self.time += 1
        nodes = self.graph["nodes"]

        # 금지 규칙 적용
        forbidden = set(self.rules.get("forbidden", []))
        for n in nodes:
            text = n.get("text", "")
            if any(tok in text for tok in forbidden):
                n["confidence"] = max(0.0, n.get("confidence", 0.5) - 0.3)

        # 단계 전이
        if self.time == 3:
            self.focus = "converge"
        if self.time == 5:
            self.focus = "execute"

        # 상위 노드 강화
        sorted_nodes = sorted(nodes, key=lambda x: x.get("confidence", 0.5), reverse=True)
        for n in sorted_nodes[:3]:
            n["importance"] = min(1.0, n.get("importance", 0.5) + 0.1)

        event = {"t": self.time, "focus": self.focus, "top": [n["id"] for n in sorted_nodes[:3]]}
        self.log.append(event)
        return event

    def run(self, steps: int = 6) -> Tuple[List[Dict], Dict]:
        events = []
        for _ in range(steps):
            events.append(self.step())

        snapshot = {
            "graph": self.graph,
            "log": self.log,
            "params": {"value_vector": self.value_vector, "rules": self.rules},
            "summary": {
                "focus_final": self.focus,
                "top_nodes": self.log[-1]["top"] if self.log else []
            }
        }
        return events, snapshot

