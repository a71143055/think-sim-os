from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.config import settings
from app.routers import chat, rules, sessions, simulation, exports, osenv

app = FastAPI(title=settings.APP_NAME)
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(rules.router, prefix="/rules", tags=["rules"])
app.include_router(sessions.router, prefix="/sessions", tags=["sessions"])
app.include_router(simulation.router, prefix="/simulation", tags=["simulation"])
app.include_router(exports.router, prefix="/exports", tags=["exports"])
app.include_router(osenv.router, prefix="/os", tags=["os"])

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
