import typer
import time
from utils import check_filename_exists
import os

app = typer.Typer()


@app.command()
def startproject(
    projectname: str = typer.Option(..., prompt="Give your project a name")
):
    typer.echo(projectname)


@app.command()
def startapp(appname: str = typer.Option(..., prompt="Give a name to your app")):
    if not os.path.exists(appname):
        try:
            pass
        except FileExistsError:
            pass


if __name__ == "__main__":
    app()
