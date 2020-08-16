from typer.testing import CliRunner

from manage_fastapi.main import app

import os

runner = CliRunner()


def test_startproject_single():
    result = runner.invoke(app, ["startproject", "test_one"], "0")
    result_two = runner.invoke(app, ["startproject", "test_two"], "1")
    assert result.exit_code == 0
    assert (
        "Project test_one created successfully!\nWe created requirements file for your project needs."
        in result.stdout
    )
    assert result_two.exit_code == 0
    assert (
        "Project test_two created successfully!\nWe created requirements file for your project needs."
        in result_two.stdout
    )
    assert os.path.isdir("./test_one")
    assert os.path.isdir("./test_one/core")
    assert os.path.isdir("./test_one/core/models")
    assert os.path.isdir("./test_one/core/schemas")
    assert os.path.isdir("./test_two")
    assert os.path.isdir("./test_two/core")
    assert os.path.isdir("./test_two/core/models")
    assert os.path.isdir("./test_two/core/schemas")


def test_startproject_duplicate():
    result = runner.invoke(app, ["startproject", "test_one"], "2")
    result_two = runner.invoke(app, ["startproject", "test_two"], "9")
    assert result.exit_code == 0
    assert "Project test_one already exists!" in result.stdout
    assert result_two.exit_code == 0
    assert "Project test_two already exists!" in result_two.stdout
