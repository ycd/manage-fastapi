from fastapi import FastAPI

from app.config import settings

app = FastAPI(title=settings.PROJECT_NAME)
