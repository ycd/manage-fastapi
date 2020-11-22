from unittest.mock import patch

import pytest
from manage_fastapi.main import app
from typer.testing import CliRunner

runner = CliRunner()

CREATED_SUCCESSFULLY = "FastAPI project created successfully! 🎉\n"
ALREADY_EXISTS = "Folder 'potato' already exists. 😞\n"


@pytest.mark.parametrize("package_", ["pip", "poetry"])
@pytest.mark.parametrize("python", ["3.6", "3.7", "3.8"])
@pytest.mark.parametrize(
    "license_", ["MIT", "BSD-3", "GNU GPL v3.0", "Apache Software License 2.0"]
)
@pytest.mark.parametrize("pre_commit", [True, False])
def test_startproject(
    project_name: str, package_: str, python: str, license_: str, pre_commit: bool
):
    package = "manage_fastapi.main.launch_cli"
    with patch(
        package, return_value=[package_, python, license_, pre_commit]
    ) as mock_obj:
        result = runner.invoke(app, ["startproject", project_name])
        assert mock_obj.assert_called_once
        assert result.output == CREATED_SUCCESSFULLY
        assert result.exit_code == 0


def test_startproject_default(project_name: str):
    result = runner.invoke(app, ["startproject", project_name, "--default"])
    assert result.output == CREATED_SUCCESSFULLY
    assert result.exit_code == 0


def test_startproject_already_exists(project_name: str):
    result = runner.invoke(app, ["startproject", project_name, "--default"])
    assert result.output == CREATED_SUCCESSFULLY
    assert result.exit_code == 0

    result = runner.invoke(app, ["startproject", project_name, "--default"])
    assert result.output == ALREADY_EXISTS
    assert result.exit_code == 0
