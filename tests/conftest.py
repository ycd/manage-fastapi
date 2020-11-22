import shutil

import pytest


@pytest.fixture
def project_name():
    name = "potato"
    yield name
    shutil.rmtree("potato")
