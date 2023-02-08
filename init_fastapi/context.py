import subprocess
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, root_validator

from init_fastapi.config import FASTAPI_VERSION
from init_fastapi.constants import Database, License, PackageManager, PythonVersion


class ProjectContext(BaseModel):
    name: str
    folder_name: str
    packaging: PackageManager

    username: Optional[str] = None
    email: Optional[EmailStr] = None

    python: PythonVersion
    fastapi: str = FASTAPI_VERSION

    license: Optional[License]
    year: int

    pre_commit: bool
    docker: bool

    database: Optional[Database]

    @root_validator(pre=True)
    def validate_project(cls, values: dict):
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

    class Config:
        use_enum_values = True
