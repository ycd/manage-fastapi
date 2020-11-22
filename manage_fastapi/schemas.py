import subprocess
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, root_validator

from manage_fastapi.config import FASTAPI_VERSION
from manage_fastapi.constants import PackageManager, PythonVersion


class Context(BaseModel):
    name: str
    folder_name: str
    packaging: PackageManager

    username: Optional[str] = None
    email: Optional[EmailStr] = None

    python: PythonVersion
    fastapi: str = FASTAPI_VERSION

    license: str
    year: int

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
        values["folder_name"] = values["name"].lower().replace(" ", "-").strip()
        values["year"] = datetime.today().year
        return values
