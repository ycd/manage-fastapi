from typer.testing import CliRunner

from manage_fastapi.main import app

runner = CliRunner()


# TODO add more tests
def test_showmodels():
    result = runner.invoke(app, ["showmodels"])
    assert result.exit_code == 0
