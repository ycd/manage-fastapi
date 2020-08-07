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
    POSTGRES_SERVER: Optional[str] = ""
    POSTGRES_USER: Optional[str] = "yagu"
    POSTGRES_PASSWORD: Optional[str] = "yagu123"
    POSTGRES_DB: Optional[str] = ""
    SQLALCHEMY_DATABASE_URL: Optional[
        str
    ] = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/mp"

    class Config:
        case_sensitive = True


settings = Settings()

