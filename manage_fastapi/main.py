import typer
from .project_utils import start_app, start_project, select_database, run_server
from .models_utils import show_models
import pkg_resources

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


@app.command(help="Runs the development server")
def runserver():
    installed_pkgs = [d.project_name for d in pkg_resources.working_set]
    if "uvicorn" not in installed_pkgs:
        print(f"Default(uvicorn) server not found in installed packages.")
    run_server()


@app.command(help="Shows all Pydantic models")
def showmodels():
    show_models()
