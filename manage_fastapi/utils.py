import pathlib
from pathlib import Path
from typing import Union
from .templates import (
    empty_main_template,
    async_sql_main_template,
    async_sql_database_template,
    tortoise_main_template,
    tortoise_database_template,
    mongo_database_template,
    mongo_main_template,
    mongo_utils_template,
    schema_template,
    settings_template,
    api_template,
    endpoint_template,
    test_template,
    requirements_template,
    database_options_template,
)


def start_project(
    project_name: str, current_path: str = Path.cwd(), database_option: str = None
):
    try:
        Path(f"{current_path}/{project_name}").mkdir(parents=True, exist_ok=False)
        Path(f"{current_path}/{project_name}/tests").mkdir(parents=True, exist_ok=False)
        Path(f"{current_path}/{project_name}/{project_name}").mkdir(
            parents=True, exist_ok=False
        )
        Path(f"{current_path}/{project_name}/{project_name}/schemas").mkdir(
            parents=True, exist_ok=False
        )
        Path(f"{current_path}/{project_name}/__init__.py").touch()
        Path(f"{current_path}/{project_name}/tests/__init__.py").touch()
        Path(
            f"{current_path}/{project_name}/{project_name}/schemas/__init__.py"
        ).touch()

        with open(
            f"{current_path}/{project_name}/{project_name}/schemas/schema.py", "a+"
        ) as schema, open(
            f"{current_path}/{project_name}/{project_name}/settings.py", "a+"
        ) as settings, open(
            f"{current_path}/requirements.txt", "a+"
        ) as requirements:
            schema.write(schema_template.replace("{project_name}", project_name))
            settings.write(settings_template.replace("{project_name}", project_name))
            requirements.write(requirements_template)

        if database_option == "0":

            Path(f"{current_path}/{project_name}/{project_name}/models").mkdir(
                parents=True, exist_ok=False
            )
            Path(
                f"{current_path}/{project_name}/{project_name}/models/__init__.py"
            ).touch()

            with open(
                f"{current_path}/{project_name}/{project_name}/models/database.py", "a+"
            ) as database, open(
                f"{current_path}/{project_name}/main.py", "a+"
            ) as main, open(
                f"{current_path}/requirements.txt", "a+"
            ) as requirements:
                database.write(
                    async_sql_database_template.replace("{project_name}", project_name)
                )
                main.write(
                    async_sql_main_template.replace("{project_name}", project_name)
                )
                requirements.write("databases[postgresql,sqlite,mysql]==0.3.2")

        # Tortoise ORM = 1
        elif database_option == "1":
            Path(f"{current_path}/{project_name}/{project_name}/models").mkdir(
                parents=True, exist_ok=False
            )
            Path(
                f"{current_path}/{project_name}/{project_name}/models/__init__.py"
            ).touch()

            with open(
                f"{current_path}/{project_name}/{project_name}/models/database.py", "a+"
            ) as database, open(
                f"{current_path}/{project_name}/main.py", "a+"
            ) as main, open(
                f"{current_path}/requirements.txt", "a+"
            ) as requirements:
                database.write(tortoise_database_template)
                main.write(
                    tortoise_main_template.replace("{project_name}", project_name)
                )
                requirements.write("tortoise-orm==0.16.14")

        # MongoDB
        elif database_option == "2":
            Path(f"{current_path}/{project_name}/{project_name}/models").mkdir(
                parents=True, exist_ok=False
            )
            Path(
                f"{current_path}/{project_name}/{project_name}/models/__init__.py"
            ).touch()

            with open(
                f"{current_path}/{project_name}/{project_name}/models/database.py", "a+"
            ) as database, open(
                f"{current_path}/{project_name}/main.py", "a+"
            ) as main, open(
                f"{current_path}/{project_name}/{project_name}/models/utils.py", "a+"
            ) as utils, open(
                f"{current_path}/requirements.txt", "a+"
            ) as requirements:
                database.write(
                    mongo_database_template.replace("{project_name}", project_name)
                )
                main.write(mongo_main_template.replace("{project_name}", project_name))
                utils.write(
                    mongo_utils_template.replace("{project_name}", project_name)
                )
                requirements.write("motor==2.1.0")

        else:
            with open(f"{current_path}/{project_name}/main.py", "a+") as main:
                main.write(empty_main_template.replace("{project_name}", project_name))

    except FileExistsError as e:
        print(f"Project {project_name} already exists!")

    else:
        print(f"Project {project_name} created successfully!")
        print(f"We created requirements file for your project needs.")


def start_app(app_name: str, current_path: str = Path.cwd()):
    try:
        Path(f"{current_path}/{app_name}").mkdir(parents=True, exist_ok=False)
        Path(f"{current_path}/{app_name}/endpoints").mkdir(parents=True, exist_ok=False)
        Path(f"{current_path}/{app_name}/__init__.py").touch()
        Path(f"{current_path}/{app_name}/endpoints/__init__.py").touch()
        Path(f"{current_path}/tests/{app_name}").mkdir(parents=True, exist_ok=False)
        Path(f"{current_path}/tests/{app_name}/__init__.py").touch()

        with open(
            f"{current_path}/{app_name}/endpoints/endpoint.py", "a+"
        ) as endpoint, open(f"{current_path}/{app_name}/api.py", "a+") as api, open(
            f"{current_path}/tests/{app_name}/test_{app_name}.py", "a+"
        ) as test:
            endpoint.write(endpoint_template.replace("{app_name}", app_name))
            api.write(api_template.replace("{app_name}", app_name))
            test.write(test_template.replace("{app_name}", app_name))

    except FileExistsError as e:
        print(f"Application {app_name} already exists!")

    else:
        print(f"Application {app_name} created successfully!")


def select_database():
    option = input(database_options_template + "Select a database: ")
    return option


# TODO
# def run_server(server: str = ("uvicorn")):
#     import os
#     import subprocess

#     project_name = os.getenv("PROJECT_NAME")
#     print(project_name)
#     subprocess.run(
#         [server, f"{Path.cwd()}/{project_name}/main:app".replace("/", "."), "--reload"]
#     )

