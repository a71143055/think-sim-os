from sqlalchemy import Column, Integer, String, JSON, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.models.base import Base

class Artifact(Base):
    __tablename__ = "artifacts"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("think_sessions.id"), index=True)
    kind = Column(String, nullable=False)  # "windows" | "workspace"
    path = Column(String, nullable=False)  # file or dir path
    meta = Column(JSON, default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())

