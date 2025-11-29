from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.graph import ThoughtGraph
from app.models.rule import RuleSet
from app.models.session import ThinkSession
from app.models.snapshot import Snapshot
from app.services.simulation_engine import SimulationState
from app.services.storage import save_snapshot_json
from app.services.workspace import write_workspace_files

router = APIRouter()

@router.post("/run")
async def run_simulation(session_id: int = Form(...), steps: int = Form(6), db: Session = Depends(get_db)):
    s = db.query(ThinkSession).filter(ThinkSession.id == session_id).first()
    g = db.query(ThoughtGraph).filter(ThoughtGraph.session_id == session_id).first()
    ruleset = db.query(RuleSet).filter(RuleSet.session_id == session_id).order_by(RuleSet.id.desc()).first()
    rules = ruleset.rules if ruleset else {}

    state = SimulationState(graph=g.graph_json, value_vector=s.value_vector, rules=rules)
    events, snapshot = state.run(steps=steps)

    snap = Snapshot(session_id=session_id, label=f"t{events[-1]['t']}", data=snapshot)
    db.add(snap); db.commit(); db.refresh(snap)
    path = save_snapshot_json(session_id, snap.label, snapshot)

    # 워크스페이스 파일 생성
    workspace_paths = write_workspace_files(session_id, snapshot, {"value_vector": s.value_vector, "rules": rules})

    return {"ok": True, "events": events, "snapshot_id": snap.id, "file": path, "workspace": workspace_paths}
