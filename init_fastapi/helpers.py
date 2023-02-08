import re
from typing import TypeVar

EnumType = TypeVar("EnumType")


def camel_to_snake(text: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()
