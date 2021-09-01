import re
from typing import Any, Dict, TypeVar, cast

import questionary

EnumType = TypeVar("EnumType")


def camel_to_snake(text: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()


def question(choices: EnumType) -> questionary.Question:
    prompt = camel_to_snake(choices.__name__).replace("_", " ")  # type: ignore
    return questionary.select(f"Select the {prompt}: ", choices=list(choices))


def binary_question(option: str) -> questionary.Question:
    return questionary.confirm(f"Do you want {option}?", default=False)


def launch_cli(**kwargs: Any) -> Dict[str, Any]:
    result = {}
    for name, question in kwargs.items():
        question = cast(questionary.Question, question)
        result[name] = question.ask()
    return result
