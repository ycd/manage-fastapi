import os
import sys
import textwrap
from pathlib import Path
from unittest.mock import patch

import pytest
from rich.console import Console
from typer.testing import CliRunner

from manage_fastapi.main import app

runner = CliRunner()


def test_routes_invalid_format(tmp_path: Path):
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(app, ["routes", str(tmp_path)])
        expected = f'"{str(tmp_path)}" is not formatted as "<module>:<app>".\n'
        assert result.output == expected
        assert result.exit_code == 1


def test_routes(tmp_path: Path):
    module = tmp_path / "main.py"
    sys.path.append(os.path.realpath(os.path.dirname(module)))
    module.write_text(
        textwrap.dedent(
            """
            from fastapi import FastAPI

            app = FastAPI()

            @app.get("/")
            def home():
                return "Hello World!"
            """
        )
    )
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(app, ["routes", "main:app"])
        assert result.exit_code == 0


def test_routes_app_not_found(tmp_path: Path):
    module = tmp_path / "main.py"
    sys.path.append(os.path.realpath(os.path.dirname(module)))
    module.write_text(
        textwrap.dedent(
            """
            from fastapi import FastAPI

            app = FastAPI()

            @app.get("/")
            def home():
                return "Hello World!"
            """
        )
    )
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(app, ["routes", "main:not_found"])
        assert result.output == '"main" does not contain an app named "not_found".\n'
        assert result.exit_code == 1
