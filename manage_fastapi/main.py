import typer
from bullet import Bullet, Input, SlidePrompt, colors

from manage_fastapi.constants import PYTHON_VERSIONS, Packaging
from manage_fastapi.generator import generate_project
from manage_fastapi.schemas import Context

app = typer.Typer(help="Managing FastAPI projects made easy!", name="Manage FastAPI")


@app.command(help="Creates a FastAPI project.")
def startproject(default: bool = typer.Option(False)):
    if default:
        context = Context(name="fastapi-project", packaging=Packaging.PIP, python="3.8")
    else:
        cli = SlidePrompt(
            [
                Input("Insert the project's name: "),
                Bullet(
                    prompt="Choose the package manager:",
                    choices=list(Packaging),
                    bullet=" >",
                    margin=2,
                    word_color=colors.foreground["white"],
                    word_on_switch=colors.foreground["white"],
                ),
                Bullet(
                    prompt="Select Python version:",
                    choices=PYTHON_VERSIONS,
                    bullet=" >",
                    margin=2,
                    word_color=colors.foreground["white"],
                    word_on_switch=colors.foreground["white"],
                ),
            ],
        )
        result = cli.launch()
        context = Context(
            name=result[0][1], packaging=result[1][1], python=result[2][1]
        )
    generate_project(context)


@app.command(help="Creates a FastAPI component.")
def startapp():
    ...
