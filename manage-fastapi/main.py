import typer
import time
from utils import start_app, start_project
import os
from pathlib import Path

app = typer.Typer(add_completion=False)


@app.command()
def startproject(
    projectname: str = typer.Option(..., prompt="Give a name to your project")
):
    start_project(projectname)


@app.command()
def startapp(appname: str = typer.Option(..., prompt="Give a name to your app")):
    start_app(appname)


if __name__ == "__main__":
    app()
