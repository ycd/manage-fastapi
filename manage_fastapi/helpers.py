import re
from typing import TypeVar

from bullet import Bullet, SlidePrompt, colors

EnumType = TypeVar("EnumType")


def camel_to_snake(text: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()


def bullet(choices: EnumType) -> Bullet:
    prompt = camel_to_snake(choices.__name__).replace("_", " ")  # type: ignore
    return Bullet(
        prompt=f"Select the {prompt}: ",
        choices=list(choices),  # type: ignore
        bullet=" >",
        margin=2,
        word_color=colors.foreground["white"],
        word_on_switch=colors.foreground["white"],
    )


def launch_cli(*prompt_objs: Bullet):
    results = SlidePrompt(prompt_objs).launch()
    return [result[1] for result in results]
