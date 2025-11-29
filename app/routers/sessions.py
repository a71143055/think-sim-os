from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.session import ThinkSession
from app.models.graph import ThoughtGraph
from app.models.rule import RuleSet
from app.models.snapshot import Snapshot

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/{session_id}")
async def session_view(session_id: int, request: Request, db: Session = Depends(get_db)):
    s = db.query(ThinkSession).filter(ThinkSession.id == session_id).first()
    g = db.query(ThoughtGraph).filter(ThoughtGraph.session_id == session_id).first()
    rules = db.query(RuleSet).filter(RuleSet.session_id == session_id).all()
    snaps = db.query(Snapshot).filter(Snapshot.session_id == session_id).order_by(Snapshot.id.desc()).all()
    return templates.TemplateResponse("session.html", {"request": request, "session": s, "graph": g.graph_json, "rules": [r.rules for r in rules], "snaps": snaps})

