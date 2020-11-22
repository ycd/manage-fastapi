import os
import subprocess

import typer

from manage_fastapi.constants import PackageManager, PythonVersion
from manage_fastapi.generator import generate_project
from manage_fastapi.helpers import bullet, launch_cli
from manage_fastapi.schemas import Context

app = typer.Typer(help="Managing FastAPI projects made easy!", name="Manage FastAPI")


@app.command(help="Creates a FastAPI project.")
def startproject(name: str, default: bool = typer.Option(False)):
    if default:
        context = Context(
            name=name, packaging=PackageManager.PIP, python=PythonVersion.THREE_DOT_EIG
        )
    else:
        result = launch_cli(bullet(PackageManager), bullet(PythonVersion))
        context = Context(name=name, packaging=result[0], python=result[1])
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
