from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.sql import func
from app.models.base import Base

class ThinkSession(Base):
    __tablename__ = "think_sessions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(String, default="created")  # created|running|paused|completed
    value_vector = Column(JSON, default={})     # {"realism":0.7,"simplicity":0.5,...}
    constraints = Column(JSON, default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())

