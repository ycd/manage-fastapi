from typing import Iterable, Tuple

from bullet import Bullet, SlidePrompt, colors


def bullet(name: str, prompt: str, choices: Iterable) -> Tuple[str, Bullet]:
    return name, Bullet(
        prompt=prompt,
        choices=choices,
        bullet=" >",
        margin=2,
        word_color=colors.foreground["white"],
        word_on_switch=colors.foreground["white"],
    )


def launch_cli(*prompt_objs: Tuple[str, Bullet]):
    result = SlidePrompt([obj[1] for obj in prompt_objs]).launch()
    return {obj[0]: result[i][1] for i, obj in enumerate(prompt_objs)}
