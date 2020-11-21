import os

from manage_fastapi.constants import Packaging

packaging = "{{ cookiecutter.packaging }}"
base_dir = os.getcwd()

remove_paths = []
if packaging == str(Packaging.PIP):
    remove_paths = ["poetry.lock", "pyproject.toml"]
elif packaging == str(Packaging.POETRY):
    remove_paths = ["requirements.txt"]


for path in remove_paths:
    path = os.path.join(base_dir, path)
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)
