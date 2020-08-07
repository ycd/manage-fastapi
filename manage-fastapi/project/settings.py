from typing import Any, Dict, List, Optional, Union

from pydantic import BaseSettings, AnyHttpUrl, HttpUrl, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI"  # Change this

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

    # or this
    SQLALCHEMY_DATABASE_URL: Optional[
        str
    ] = "postgresql://user:password@localhost:5432/db_name"

    class Config:
        case_sensitive = True


settings = Settings()

