import typer
from .utils import start_app, start_project

app = typer.Typer(add_completion=False, help="Managing FastAPI projects made easy!")


@app.command(help="Creates a project with the given name.")
def startproject(projectname: str = typer.Argument(...)):
    start_project(projectname)


@app.command(help="Creates a app with the given name.")
def startapp(appname: str = typer.Argument(...)):
    start_app(appname)
