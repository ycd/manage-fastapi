import os
from typing import TypeVar

import typer
from cookiecutter.exceptions import OutputDirExistsException
from cookiecutter.main import cookiecutter
from pydantic.main import BaseModel

from manage_fastapi.config import TEMPLATES_DIR
from manage_fastapi.context import AppContext, ProjectContext

ContextType = TypeVar("ContextType", bound=BaseModel)


def fill_template(template_name: str, context: ContextType):
    try:
        cookiecutter(
            os.path.join(TEMPLATES_DIR, template_name),
            extra_context=context.dict(),
            no_input=True,
        )
    except OutputDirExistsException:
        typer.echo(f"Folder '{context.folder_name}' already exists. 😞")
    else:
        typer.echo(f"FastAPI {template_name} created successfully! 🎉")


def generate_app(context: AppContext):
    fill_template("app", context)


def generate_project(context: ProjectContext):
    fill_template("project", context)
