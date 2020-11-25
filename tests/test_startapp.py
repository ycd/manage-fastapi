from typer.testing import CliRunner

from manage_fastapi.main import app

runner = CliRunner()

CREATED_SUCCESSFULLY = "FastAPI app created successfully! 🎉\n"
ALREADY_EXISTS = "Folder 'potato' already exists. 😞\n"


def test_startproject_default(project_name: str):
    result = runner.invoke(app, ["startapp", project_name])
    assert result.output == CREATED_SUCCESSFULLY
    assert result.exit_code == 0
