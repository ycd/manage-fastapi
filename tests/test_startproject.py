from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from manage_fastapi.main import app

runner = CliRunner()


@pytest.mark.parametrize("pkg", ["pip", "poetry"])
@pytest.mark.parametrize("py", ["3.6", "3.7", "3.8", "3.9"])
def test_startproject(project_name: str, pkg: str, py: str):
    package = "manage_fastapi.main.launch_cli"
    with patch(package, return_value={"pkg": pkg, "py": py}) as mock_obj:
        result = runner.invoke(app, ["startproject", project_name])
        assert mock_obj.assert_called_once
        assert "FastAPI project created successfully! 🎉\n" in result.output
        assert result.exit_code == 0


def test_startproject_default(project_name: str):
    result = runner.invoke(app, ["startproject", project_name, "--default"])
    assert "FastAPI project created successfully! 🎉\n" in result.output
    assert result.exit_code == 0
