import subprocess
from typing import Optional

from pydantic import BaseModel, EmailStr, root_validator, validator

from manage_fastapi.config import FASTAPI_VERSION
from manage_fastapi.constants import PYTHON_VERSIONS, Packaging


class Context(BaseModel):
    name: str
    packaging: Packaging

    username: Optional[str] = None
    email: Optional[EmailStr] = None

    python: str
    fastapi: str = FASTAPI_VERSION

    @root_validator(pre=True)
    def git_info(cls, values: dict):
        try:
            values["username"] = subprocess.check_output(
                ["git", "config", "--get", "user.name"]
            )
            values["email"] = subprocess.check_output(
                ["git", "config", "--get", "user.email"]
            )
        except subprocess.CalledProcessError:
            ...
        return values

    @validator("python")
    def validate_python_version(cls, value: str):
        if value not in PYTHON_VERSIONS:
            raise ValueError(f"Invalid Python version: {value}.")
        return value
