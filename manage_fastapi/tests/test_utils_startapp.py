from typer.testing import CliRunner

from manage_fastapi.main import app

runner = CliRunner()


def test_startapp_single():
    result = runner.invoke(app, ["startapp", "myapp"])
    assert result.exit_code == 0
    assert "Application myapp created successfully!" in result.stdout


def test_startapp_duplicate():
    result = runner.invoke(app, ["startapp", "myapp"])
    assert result.exit_code == 0
    assert "Application myapp already exists!" in result.stdout
