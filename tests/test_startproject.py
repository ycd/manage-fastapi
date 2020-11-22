from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from manage_fastapi.main import app

runner = CliRunner()

CREATED_SUCCESSFULLY = "FastAPI project created successfully! 🎉\n"
ALREADY_EXISTS = "Folder 'potato' already exists. 😞\n"


@pytest.mark.parametrize("pkg", ["pip", "poetry"])
@pytest.mark.parametrize("py", ["3.6", "3.7", "3.8", "3.9"])
def test_startproject(project_name: str, pkg: str, py: str):
    package = "manage_fastapi.main.launch_cli"
    with patch(package, return_value=[pkg, py]) as mock_obj:
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
