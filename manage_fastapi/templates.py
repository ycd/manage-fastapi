database_options_template = """[0] PostgreSQL - SQLite - MySQL 
[1] Tortoise                    
[2] MongoDB                     
[9] Create without Database     

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
    DB_SERVER: Optional[str] = ""
    DB_USER: Optional[str] = ""
    DB_PASSWORD: Optional[str] = ""
    DB_PORT: Optional[str] = ""
    DB_NAME: Optional[str] = ""
    DB_PORT: Optional[str] = ""

    # DATABASE_URL: str = f"{DB_SERVER}://{DB_USER}:{DB_PASSWORD}@{DB_PORT}:{DB_PORT}/{DB_NAME}"
    
    DATABASE_URL = "sqlite:///./test.db"



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
# if you want to include this router to your app
# go to your main.py then add this 
# from {app_name}.api import api_router as {app_name}_router




from fastapi import APIRouter

from {app_name}.endpoints import endpoint

api_router = APIRouter()
api_router.include_router(endpoint.router, prefix="/{app_name}", tags=["{app_name}"])
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

requirements_template = """fastapi==0.61.0
uvicorn==0.11.8
"""


# TORTOISE Main | Database template

tortoise_main_template = """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.models.database import Example
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise


from core.settings import settings

app = FastAPI(title=settings.PROJECT_NAME)


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_methods=["*"],
        allow_headers=["*"],
    )



register_tortoise(
    app,
    db_url=settings.DATABASE_URL,
    modules={"models": ["{project_name}.core.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
"""

tortoise_database_template = """from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Example(models.Model):

    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class PydanticMeta:
        pass


Example = pydantic_model_creator(Example, name="Example")
"""


# Postgresql, SQLite, MySQL Main | Database

empty_main_template = """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.settings import settings 

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_methods=["*"],
        allow_headers=["*"],
    )


"""


async_sql_main_template = """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.settings import settings 
from core.models.database import database

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

async_sql_database_template = """import sqlalchemy
from core.settings import settings
import databases

database = databases.Database(settings.DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Put your database models here | Below

# FastAPI documentation for databases: https://fastapi.tiangolo.com/advanced/async-sql-databases/

# Put your database models here | Above


engine = sqlalchemy.create_engine(settings.DATABASE_URL)
metadata.create_all(engine)
"""


### MONGODB
mongo_main_template = """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.settings import settings 
from core.models.utils import connect_to_mongo, close_mongo_connection

app = FastAPI()

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)


"""


mongo_database_template = """from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.client
"""

mongo_utils_template = """import logging

from motor.motor_asyncio import AsyncIOMotorClient
from core.models.database import db

logger = logging.getLogger(__name__)


async def connect_to_mongo():
    db.client = AsyncIOMotorClient(str("localhost:27017"),
                                   maxPoolSize=10,
                                   minPoolSize=10)

    logger.info(f"Connecting to mongoDB")


async def close_mongo_connection():
    db.client.close()
    logger.info(f"Closing to mongoDB")
"""
