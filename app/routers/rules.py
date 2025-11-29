from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.rule import RuleSet
import json

router = APIRouter()

@router.post("/apply")
async def apply_rules(session_id: int = Form(...), name: str = Form(...), rules_json: str = Form(...), db: Session = Depends(get_db)):
    rules = json.loads(rules_json)
    rs = RuleSet(session_id=session_id, name=name, rules=rules)
    db.add(rs); db.commit()
    return {"ok": True, "rule_set_id": rs.id}

