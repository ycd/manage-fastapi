import re
from typing import Tuple, TypeVar

from bullet import Bullet, SlidePrompt, colors
from bullet.client import YesNo

EnumType = TypeVar("EnumType")

WHITE_FOREGROUND = colors.foreground["white"]


def camel_to_snake(text: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()


def bullet(choices: EnumType) -> Bullet:
    prompt = camel_to_snake(choices.__name__).replace("_", " ")  # type: ignore
    return Bullet(
        prompt=f"Select the {prompt}: ",
        choices=list(choices),  # type: ignore
        bullet=" >",
        margin=2,
        word_color=WHITE_FOREGROUND,
        word_on_switch=WHITE_FOREGROUND,
    )


def yes_no(option: str) -> YesNo:
    return YesNo(
        prompt=f"Do you want {option}?", default="n", word_color=WHITE_FOREGROUND
    )


def launch_cli(*prompt_objs: Tuple[str, Bullet]):
    names, objs = zip(*prompt_objs)
    results = SlidePrompt(objs).launch()
    return {name: result[1] for name, result in zip(names, results)}
