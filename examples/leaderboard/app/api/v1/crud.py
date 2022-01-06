from typing import Any
import random, time
from uuid import uuid4
from pydantic.types import UUID1

from sqlalchemy.engine import create_engine
from app.app.core.models.model import Score, User, UserCreate
from fastapi import APIRouter
from pydantic import BaseModel
from app.app.database import (
    database,
    user_table,
    score_table,
    CREATE_LEADERBOARD_VIEW,
    CREATE_USERS_WITH_SCORES_VIEW,
    GET_LEADERBOARD,
    CREATE_SCORE_TABLE,
    CREATE_USERS_TABLE,
)

router = APIRouter()


@router.on_event("startup")
async def connect_database():
    await database.connect()
    await database.execute(CREATE_USERS_TABLE)
    await database.execute(CREATE_SCORE_TABLE)
    await database.execute(CREATE_USERS_WITH_SCORES_VIEW)
    await database.execute(CREATE_LEADERBOARD_VIEW)


@router.on_event("shutdown")
async def disconnect_database():
    await database.disconnect()


class Response(BaseModel):
    error: str
    success: bool
    data: Any


@router.post("/user/create")
async def create_user(user: UserCreate):
    user_id = str(uuid4())[:40]
    query = user_table.insert()
    values = {"user_id": user_id, "name": user.display_name, "country": user.country}
    await database.execute(query=query, values=values)
    return Response(error="", success=True, data={"user_id": user_id})


@router.get("/leaderboard")
async def leaderboard():
    rows = await database.fetch_all(GET_LEADERBOARD)
    return Response(success=True, error="", data=rows)


@router.post("/score/submit")
async def submit_score(score: Score):
    query = score_table.insert()
    values = {"user_id": score.user_id, "point": score.score}
    await database.execute(query=query, values=values)
    return Response(error="", success=True, data={})