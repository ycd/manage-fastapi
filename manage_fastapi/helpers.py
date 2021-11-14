import re
from importlib import import_module
from typing import TypeVar

import questionary

EnumType = TypeVar("EnumType")


def camel_to_snake(text: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()


def question(choices: EnumType) -> questionary.Question:
    prompt = camel_to_snake(choices.__name__).replace("_", " ")  # type: ignore
    return questionary.select(f"Select the {prompt}: ", choices=list(choices))


def binary_question(option: str) -> questionary.Question:
    return questionary.confirm(f"Do you want {option}?", default=False)


def import_from_string(dotted_path: str) -> object:
    try:
        module_path, app_name = dotted_path.rsplit(":", 1)
    except ValueError:
        raise SystemExit(f'"{dotted_path}" is not formatted as "<module>:<app>".')

    module = import_module(module_path)
    try:
        return getattr(module, app_name)
    except AttributeError:
        raise SystemExit(f'"{module_path}" does not contain an app named "{app_name}".')
