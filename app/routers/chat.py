from fastapi import APIRouter, Depends, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.session import ThinkSession
from app.models.graph import ThoughtGraph
from app.services.graph_builder import build_graph_from_chat, serialize_graph

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/new", response_class=HTMLResponse)
async def chat_form():
    html = """
    <form hx-post="/chat/ingest" hx-target="#result">
      <textarea name="text" rows="8" style="width:100%" placeholder="당신의 생각을 입력하세요"></textarea>
      <input type="text" name="session_name" placeholder="Session name"/>
      <button type="submit">Create session</button>
    </form>
    <div id="result"></div>
    """
    return HTMLResponse(html)

@router.post("/ingest", response_class=HTMLResponse)
async def ingest(text: str = Form(...), session_name: str = Form(...), db: Session = Depends(get_db)):
    value_vector = {"realism": 0.7, "simplicity": 0.6, "explainability": 0.7}
    session = ThinkSession(name=session_name, value_vector=value_vector)
    db.add(session); db.commit(); db.refresh(session)

    chat_items = [{"role": "user", "text": text}]
    G = build_graph_from_chat(chat_items, value_vector)
    graph_json = serialize_graph(G)

    tg = ThoughtGraph(session_id=session.id, graph_json=graph_json)
    db.add(tg); db.commit()

    return HTMLResponse(f"<p>Session created: {session.id}</p><a href='/sessions/{session.id}'>Open</a>")
