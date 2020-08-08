import pathlib
from pathlib import Path
from typing import Union
from .templates import (
    main_template,
    database_template,
    schema_template,
    settings_template,
    api_template,
    endpoint_template,
    test_template,
)


def start_project(project_name: str, current_path: str = Path.cwd()):
    try:
        Path(f"{current_path}/{project_name}").mkdir(parents=True, exist_ok=False)
        Path(f"{current_path}/{project_name}/tests").mkdir(parents=True, exist_ok=False)
        Path(f"{current_path}/{project_name}/{project_name}").mkdir(
            parents=True, exist_ok=False
        )
        Path(f"{current_path}/{project_name}/{project_name}/schemas").mkdir(
            parents=True, exist_ok=False
        )
        Path(f"{current_path}/{project_name}/{project_name}/models").mkdir(
            parents=True, exist_ok=False
        )
        Path(f"{current_path}/{project_name}/__init__.py").touch()
        Path(f"{current_path}/{project_name}/tests/__init__.py").touch()
        Path(f"{current_path}/{project_name}/{project_name}/models/__init__.py").touch()
        Path(
            f"{current_path}/{project_name}/{project_name}/schemas/__init__.py"
        ).touch()

        with open(f"{current_path}/{project_name}/main.py", "a+") as main, open(
            f"{current_path}/{project_name}/{project_name}/schemas/schema.py", "a+"
        ) as schema, open(
            f"{current_path}/{project_name}/{project_name}/models/database.py", "a+"
        ) as database, open(
            f"{current_path}/{project_name}/{project_name}/settings.py", "a+"
        ) as settings:
            main.write(main_template.replace("{project_name}", project_name))

            schema.write(schema_template.replace("{project_name}", project_name))
            database.write(database_template.replace("{project_name}", project_name))
            settings.write(settings_template.replace("{project_name}", project_name))

    except FileExistsError as e:
        print(f"Project {project_name} already exists!", e)


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
        print(f"App {app_name} already exists!", e)
