import os
import orjson
from typing import Dict
from app.config import settings

def ensure_workspace(session_id: int) -> str:
    base = os.path.join(settings.WORKSPACE_DIR, f"session_{session_id}")
    os.makedirs(base, exist_ok=True)
    return base

def write_workspace_files(session_id: int, snapshot: Dict, config: Dict) -> Dict:
    base = ensure_workspace(session_id)
    paths = {}

    paths["config"] = os.path.join(base, "config.json")
    with open(paths["config"], "wb") as f:
        f.write(orjson.dumps(config))

    paths["snapshot"] = os.path.join(base, "snapshot.json")
    with open(paths["snapshot"], "wb") as f:
        f.write(orjson.dumps(snapshot))

    paths["readme"] = os.path.join(base, "README.txt")
    with open(paths["readme"], "w", encoding="utf-8") as f:
        f.write("이 폴더는 사고 시뮬레이션 결과 워크스페이스입니다.\n")
        f.write("config.json: 가치/규칙 등 설정\n")
        f.write("snapshot.json: 그래프/로그/요약\n")

    # 간단한 합성 브리프
    brief_path = os.path.join(base, "synthesis_brief.md")
    summary = snapshot.get("summary", {})
    with open(brief_path, "w", encoding="utf-8") as f:
        f.write("# 합성 브리프\n\n")
        f.write(f"- 최종 포커스: {summary.get('focus_final','')}\n")
        f.write(f"- 우선 노드: {', '.join(summary.get('top_nodes', []))}\n")
        f.write("\n## 다음 단계\n- 테스트 체크리스트 작성\n- 실행 태스크 정의\n")
    paths["brief"] = brief_path

    return {"base": base, **paths}

