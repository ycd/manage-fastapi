from typing import Optional

import pkg_resources
import typer

from init_fastapi.constants import Database, License, PackageManager, PythonVersion
from init_fastapi.context import ProjectContext
from init_fastapi.generator import generate_project

app = typer.Typer(
    add_completion=False,
    help="Init FastAPI projects made easy!",
    name="Init FastAPI",
)


@app.command(help="Creates a FastAPI project.")
def init(
    name: str,
    database: Optional[Database] = typer.Option(None, case_sensitive=False),
    docker: bool = typer.Option(False),
    license_: Optional[License] = typer.Option(None, "--license", case_sensitive=False),
    packaging: PackageManager = typer.Option(PackageManager.PIP),
    pre_commit: bool = typer.Option(False, "--pre-commit"),
    python: PythonVersion = typer.Option(PythonVersion.THREE_DOT_EIG),
):

    context = ProjectContext(
        name=name,
        packaging=packaging,
        python=python,
        license=license_,
        pre_commit=pre_commit,
        docker=docker,
        database=database,
    )

    generate_project(context)

def version_callback(value: bool):
    if value:
        version = pkg_resources.get_distribution("manage-fastapi").version
        typer.echo(f"manage-fastapi, version {version}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show the Manage FastAPI version information.",
    )
):
    ...
