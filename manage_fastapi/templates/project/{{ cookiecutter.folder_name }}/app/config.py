from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str

    class Config:
        env_file = ".env"


settings = Settings()
