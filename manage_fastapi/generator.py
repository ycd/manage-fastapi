import os

import typer
from cookiecutter.exceptions import OutputDirExistsException
from cookiecutter.main import cookiecutter

from manage_fastapi.config import TEMPLATES_DIR
from manage_fastapi.schemas import Context


def generate_project(context: Context):
    try:
        cookiecutter(
            os.path.join(TEMPLATES_DIR, "project"),
            extra_context=context.dict(),
            no_input=True,
        )
        typer.echo(f'"{context.name}" created successfully! 🎉')
    except OutputDirExistsException:
        typer.echo(f'"{context.name}" already exists. 😞')
