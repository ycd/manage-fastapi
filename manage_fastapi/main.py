import os
import subprocess

import typer

from manage_fastapi.constants import Database, License, PackageManager, PythonVersion
from manage_fastapi.generator import generate_project
from manage_fastapi.helpers import bullet, launch_cli, yes_no
from manage_fastapi.schemas import Context

app = typer.Typer(help="Managing FastAPI projects made easy!", name="Manage FastAPI")


@app.command(help="Creates a FastAPI project.")
def startproject(name: str, default: bool = typer.Option(False)):
    if default:
        context = Context(
            name=name,
            packaging=PackageManager.PIP,
            python=PythonVersion.THREE_DOT_EIG,
            license=License.MIT,
            pre_commit=True,
            docker=True,
            database=Database.NONE,
        )
    else:
        result = launch_cli(
            ("packaging", bullet(PackageManager)),
            ("python", bullet(PythonVersion)),
            ("license", bullet(License)),
            ("pre_commit", yes_no("pre commit")),
            ("docker", yes_no("docker")),
            ("database", bullet(Database)),
        )
        context = Context(name=name, **result)
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
