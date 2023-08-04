from pydantic import BaseModel
from typing import List


class UserCreate(BaseModel):
    country: str
    display_name: str


class User(BaseModel):
    user_id: str
    country: str
    display_name: str


class Score(BaseModel):
    user_id: str
    score: int


class UserScore(BaseModel):
    user_id: str
    score: int
    country: str
    display_name: str


class Leaderboard(BaseModel):
    data: List[UserScore]
