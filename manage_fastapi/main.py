import typer
from .utils import start_app, start_project, select_database


app = typer.Typer(
    add_completion=False,
    help="Managing FastAPI projects made easy!",
    name="Manage FastAPI",
)


@app.command(help="Creates a project with the given name.")
def startproject(projectname: str = typer.Argument(...)):
    database_option = select_database()
    start_project(projectname, database_option=database_option)


@app.command(help="Creates a app with the given name.")
def startapp(appname: str = typer.Argument(...)):
    start_app(appname)


# TODO
# @app.command(help="Runs server")
# def runserver(server: str = typer.Argument("uvicorn")):
#     run_server()

