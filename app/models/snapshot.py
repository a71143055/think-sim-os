from sqlalchemy import Column, Integer, String, JSON, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.models.base import Base

class Snapshot(Base):
    __tablename__ = "snapshots"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("think_sessions.id"), index=True)
    label = Column(String, nullable=False)
    data = Column(JSON, default={})  # {"graph":..., "log":..., "params":...}
    created_at = Column(DateTime(timezone=True), server_default=func.now())

