import os
import subprocess

import typer

from manage_fastapi.constants import PYTHON_VERSIONS, Packaging
from manage_fastapi.generator import generate_project
from manage_fastapi.helpers import bullet, launch_cli
from manage_fastapi.schemas import Context

app = typer.Typer(help="Managing FastAPI projects made easy!", name="Manage FastAPI")


@app.command(help="Creates a FastAPI project.")
def startproject(name: str, default: bool = typer.Option(False)):
    if default:
        context = Context(name=name, packaging=Packaging.PIP, python="3.8")
    else:
        result = launch_cli(
            bullet(
                name="pkg",
                prompt="Choose the package manager:",
                choices=list(Packaging),
            ),
            bullet(name="py", prompt="Select Python version:", choices=PYTHON_VERSIONS),
        )
        context = Context(name=name, packaging=result["pkg"], python=result["py"])
    generate_project(context)


@app.command(help="Creates a FastAPI component.")
def startapp():
    ...


@app.command(help="Run a FastAPI application.")
def run(prod: bool = typer.Option(False)):
    args = []
    if not prod:
        args.append("--reload")
    app_file = os.getenv("FASTAPI_APP", "app.main")
    subprocess.call(["uvicorn", f"{app_file}:app", *args])
