import os
from pydantic import BaseModel

class Settings(BaseModel):
    APP_NAME: str = os.getenv("APP_NAME", "ThinkSimOS")
    DB_URL: str = os.getenv("DB_URL", "sqlite:///./app/db.sqlite3")
    SNAPSHOT_DIR: str = os.getenv("SNAPSHOT_DIR", "./data/snapshots")
    EXPORT_DIR: str = os.getenv("EXPORT_DIR", "./data/exports")
    WORKSPACE_DIR: str = os.getenv("WORKSPACE_DIR", "./workspace")

settings = Settings()
