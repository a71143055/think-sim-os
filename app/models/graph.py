from sqlalchemy import Column, Integer, JSON, ForeignKey
from app.models.base import Base

class ThoughtGraph(Base):
    __tablename__ = "thought_graphs"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("think_sessions.id"), index=True)
    graph_json = Column(JSON, default={})  # nodes/edges serialized

