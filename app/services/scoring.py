from typing import Dict, Any

def decision_score(node: Dict[str, Any], value_vector: Dict[str, float]) -> float:
    importance = float(node.get("importance", 0.5))
    confidence = float(node.get("confidence", 0.5))
    realism_w = value_vector.get("realism", 0.5)
    simplicity_w = value_vector.get("simplicity", 0.5)
    return importance * 0.5 + confidence * 0.5 + 0.2 * realism_w + 0.1 * simplicity_w
