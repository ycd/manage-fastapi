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
    if packaging == PackageManager.PIP:
        remove_paths(["poetry.lock", "pyproject.toml"])
    elif packaging == PackageManager.POETRY:
        remove_paths(["requirements.txt"])


def set_pre_commit():
    pre_commit: bool = eval("{{ cookiecutter.pre_commit }}")
    if pre_commit is False:
        remove_paths([".pre-commit-config.yaml", "setup.cfg"])


def set_docker():
    docker: bool = eval("{{ cookiecutter.docker }}")
    if docker is False:
        remove_paths(["Dockerfile", "docker-compose.yaml"])


def set_database():
    database = "{{ cookiecutter.database }}"
    if database == "None":
        remove_paths(["app/database.py"])


def set_license():
    license_ = "{{ cookiecutter.license }}"
    if license_ == "None":
        remove_paths(["LICENSE"])


# TODO(Marcelo): Alter config.py location according to the project complexity.
# def set_config_location():
#     database = "{{ cookiecutter.database }}"
#     if database == "None":
#         remove_paths(["app/core/config.py"])
#     else:
#         remove_paths(["app/config.py"])


def main():
    set_database()
    set_docker()
    set_license()
    set_packaging()
    set_pre_commit()


if __name__ == "__main__":
    main()
