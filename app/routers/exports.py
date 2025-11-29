from fastapi import APIRouter, Depends, Form
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.session import ThinkSession
from app.models.snapshot import Snapshot
from app.services.workspace import write_workspace_files
from app.services.exporter import create_windows_artifact

router = APIRouter()

@router.post("/windows")
async def export_windows(session_id: int = Form(...), db: Session = Depends(get_db)):
    s = db.query(ThinkSession).filter(ThinkSession.id == session_id).first()
    snap = db.query(Snapshot).filter(Snapshot.session_id == session_id).order_by(Snapshot.id.desc()).first()
    if not snap:
        return {"ok": False, "error": "No snapshot found"}

    workspace_paths = write_workspace_files(session_id, snap.data, {"value_vector": s.value_vector})
    zip_path = create_windows_artifact(session_id, workspace_paths)
    return {"ok": True, "zip": zip_path}

@router.get("/download")
async def download(path: str):
    return FileResponse(path, filename=path.split("/")[-1], media_type="application/zip")
