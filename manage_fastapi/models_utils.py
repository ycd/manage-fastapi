import os
from pathlib import Path
from typing import Dict


def find_models() -> Dict[str, str]:
    main_path = ""
    result = {}

    for path, directories, files in os.walk(str(Path.cwd())):
        if "schemas" in directories:
            main_path = path + "/schemas"
            break

    for path, directories, files in os.walk(main_path):
        for file in files:

            class_name_list = []
            if not file.startswith("__"):
                with open(f"{path}/{file}", "r") as f:
                    for line in f.read().splitlines():
                        if line.startswith("class"):
                            class_name = "".join(
                                [i for i in (line.replace(" ", "(")).split("(")][1]
                            ).replace(":", "")
                            class_name_list.append(class_name)

                result.update({file: class_name_list})
    return result


def msg_box(msg: str, indent: int = 1, width: int = None, title: str = None) -> str:
    space = " " * indent
    if not width:
        width = max((map(len, msg)))
    box = f'╔{"═" * (width + indent * 2)}╗\n'
    if title:
        box += f"║{space}{title:<{width}}{space}║\n"
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'
    box += "".join([f"║{space}{line:<{width}}{space}║\n" for line in msg])
    box += f'╚{"═" * (width + indent * 2)}╝'
    return box


def show_models() -> str:
    models = find_models()
    for key, value in models.items():
        print(msg_box(msg=value, title=key, width=30))
