from typer.testing import CliRunner

from manage_fastapi.main import app

runner = CliRunner()


def test_startproject_single():
    result = runner.invoke(app, ["startproject", "myproject"], "0")
    assert result.exit_code == 0
    assert (
        "Project myproject created successfully!\nWe created requirements file for your project needs."
        in result.stdout
    )


def test_startproject_duplicate():
    result = runner.invoke(app, ["startproject", "myproject"], "2")
    assert result.exit_code == 0
    assert "Project myproject already exists!" in result.stdout

