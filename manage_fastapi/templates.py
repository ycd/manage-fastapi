main_template = """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from {project_name}.settings import settings
from {project_name}.models.database import database

app = FastAPI(title=settings.PROJECT_NAME)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.on_event("startup")
async def connect_database():
    await database.connect()


@app.on_event("shutdown")
async def disconnect_database():
    await database.disconnect()
"""

schema_template = """# For more information check Pydantic documentation = https://pydantic-docs.helpmanual.io/usage/models/
#
# Creating your custom classes
#
# class ClassName(BaseModel):
#     name: str
#     value: int
#

from pydantic import BaseModel, Field


class Model(BaseModel):
    pass
"""

database_template = """import sqlalchemy
from {project_name}.settings import settings
import databases

database = databases.Database(settings.SQLALCHEMY_DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Put your database models here | Below

# FastAPI documentation for databases: https://fastapi.tiangolo.com/advanced/async-sql-databases/

# Put your database models here | Above


engine = sqlalchemy.create_engine(settings.SQLALCHEMY_DATABASE_URL)
metadata.create_all(engine)
"""

settings_template = """from typing import Any, Dict, List, Optional, Union

from pydantic import BaseSettings, AnyHttpUrl, HttpUrl, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "{project_name}" 

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost",
        "http://localhost:80",
        "http://localhost:8000",
    ]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # Database Settings
    DATABASE_SERVER: Optional[str] = ""
    DATABASE_USER: Optional[str] = ""
    DATABASE_PASSWORD: Optional[str] = ""
    DATABASE_PORT: Optional[str] = ""
    DATABASE_NAME: Optional[str] = ""
    DATABASE_HOST: Optional[str] = ""

    # SQLALCHEMY_DATABASE_URL: Optional[
    #     str
    # ] = f"{DATABASE_SERVER}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

    
    # SQLALCHEMY_DATABASE_URL = "postgresql://user:passowrd@localhost:5432/database_name"
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"



    class Config:
        case_sensitive = True


settings = Settings()
"""

endpoint_template = """from fastapi import APIRouter, Body, Depends


router = APIRouter()


@router.get("/")
async def hello_fastapi():
    return {"Hello":"FastAPI"}
"""


api_template = """# This is an example of how you can route and you are free to change 
# this will not affect your be included unless you add
# from {app_name}.api import api_router
# to your main.py on your project folder


from fastapi import APIRouter

from {app_name}.endpoints import endpoint

api_router = APIRouter()
api_router.include_router(endpoint.router, prefix="/hello", tags=["{app_name}"])
"""

test_template = """from fastapi.testclient import TestClient
from {app_name}.api import api_router as app

items = {}

client = TestClient(app)

@app.get("/hello")
async def get_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"Hello": "FastAPI"}

@app.on_event("startup")
async def startup_event():
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}


@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]


def test_read_items():
    response = client.get("/items/foo")
    assert response.status_code == 200
    assert response.json() == {"name": "Fighters"}
"""
