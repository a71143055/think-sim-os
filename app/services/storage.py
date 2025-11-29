import orjson
import os
from app.config import settings

def save_snapshot_json(session_id: int, label: str, snapshot: dict) -> str:
    os.makedirs(settings.SNAPSHOT_DIR, exist_ok=True)
    fname = f"{settings.SNAPSHOT_DIR}/session_{session_id}_{label}.json"
    with open(fname, "wb") as f:
        f.write(orjson.dumps(snapshot))
    return fname
