import os

from manage_fastapi.constants import PackageManager


def remove_paths(paths: list):
    base_dir = os.getcwd()

    for path in paths:
        path = os.path.join(base_dir, path)
        if path and os.path.exists(path):
            if os.path.isdir(path):
                os.rmdir(path)
            else:
                os.unlink(path)


def set_packaging():
    packaging = "{{ cookiecutter.packaging }}"
    paths = []

    if packaging == str(PackageManager.PIP):
        paths = ["poetry.lock", "pyproject.toml"]
    elif packaging == str(PackageManager.POETRY):
        paths = ["requirements.txt"]

    remove_paths(paths)


def set_pre_commit():
    pre_commit: bool = eval("{{ cookiecutter.pre_commit }}")
    if pre_commit is False:
        remove_paths([".pre-commit-config.yaml"])


def main():
    set_packaging()
    set_pre_commit()


if __name__ == "__main__":
    main()
