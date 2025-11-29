from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from app.models.base import Base

class RuleSet(Base):
    __tablename__ = "rule_sets"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("think_sessions.id"), index=True)
    name = Column(String, nullable=False)
    rules = Column(JSON, default={})  # {"forbidden":["X"],"priorities":{"realism":0.8},...}

