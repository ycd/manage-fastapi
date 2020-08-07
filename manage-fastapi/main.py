from project.settings import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from project.models.database import database, test

app = FastAPI(title=settings.PROJECT_NAME)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.on_event("startup")
async def connect_database():
    await database.connect()


@app.on_event("shutdown")
async def disconnect_database():
    await database.disconnect()


@app.post("test")
async def test():
    query = database.test.insert().values(id=1, name="test")
    await database.execute(query)
    return ""
