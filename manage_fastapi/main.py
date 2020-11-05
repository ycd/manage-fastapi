import pkg_resources
import typer


from .project_utils import select_database, start_app, start_project

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
