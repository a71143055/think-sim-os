from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import os
from app.dependencies import get_db
from app.config import settings

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def list_workspace():
    base = settings.WORKSPACE_DIR
    items = []
    if not os.path.isdir(base):
        return items
    for name in os.listdir(base):
        p = os.path.join(base, name)
        if os.path.isdir(p):
            files = [{"name": f, "path": os.path.join(p, f)} for f in os.listdir(p)]
            items.append({"dir": name, "files": files})
    return items

@router.get("/env")
async def os_view(request: Request, db: Session = Depends(get_db)):
    items = list_workspace()
    return templates.TemplateResponse("os.html", {"request": request, "items": items})
