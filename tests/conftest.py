import shutil

import pytest


@pytest.fixture
def project_name():
    name = "potato"
    yield name
    try:
        shutil.rmtree(name)
    except FileNotFoundError:
        ...
