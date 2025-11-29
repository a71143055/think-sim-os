from sqlalchemy import create_engine
from app.models.base import Base
from app.models.session import ThinkSession
from app.models.rule import RuleSet
from app.models.graph import ThoughtGraph
from app.models.snapshot import Snapshot
from app.models.artifact import Artifact
from app.config import settings

def init():
    engine = create_engine(settings.DB_URL, future=True)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()

