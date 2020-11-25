from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from manage_fastapi.main import app

runner = CliRunner()

CREATED_SUCCESSFULLY = "FastAPI project created successfully! 🎉\n"
ALREADY_EXISTS = "Folder 'potato' already exists. 😞\n"


@pytest.mark.parametrize("packaging", ["pip", "poetry"])
@pytest.mark.parametrize("python", ["3.6", "3.7", "3.8"])
@pytest.mark.parametrize("license_", ["MIT", "BSD", "GNU", "Apache"])
@pytest.mark.parametrize("pre_commit", [True, False])
@pytest.mark.parametrize("docker", [True, False])
@pytest.mark.parametrize("database", ["Postgres"])
def test_startproject(
    project_name: str,
    packaging: str,
    python: str,
    license_: str,
    pre_commit: bool,
    docker: bool,
    database: str,
):
    package = "manage_fastapi.main.launch_cli"
    with patch(package) as mock_obj:

        def side_effect(*args):
            return {
                "packaging": packaging,
                "python": python,
                "license": license_,
                "pre_commit": pre_commit,
                "docker": docker,
                "database": database,
            }

        mock_obj.side_effect = side_effect
        result = runner.invoke(app, ["startproject", project_name, "--interact"])
        assert mock_obj.assert_called_once
        assert result.output == CREATED_SUCCESSFULLY
        assert result.exit_code == 0


def test_startproject_default(project_name: str):
    result = runner.invoke(app, ["startproject", project_name])
    assert result.output == CREATED_SUCCESSFULLY
    assert result.exit_code == 0


def test_startproject_already_exists(project_name: str):
    result = runner.invoke(app, ["startproject", project_name])
    assert result.output == CREATED_SUCCESSFULLY
    assert result.exit_code == 0

    result = runner.invoke(app, ["startproject", project_name])
    assert result.output == ALREADY_EXISTS
    assert result.exit_code == 0
