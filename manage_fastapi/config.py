import os

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "templates")
version = None
try:
    
    from importlib.metadata import version
    FASTAPI_VERSION = version("fastapi")
    DYNACONF_VERSION = version("dynaconf")
    LOGURU_VERSION = version("loguru")
    
except ModuleNotFoundError:
    pass

try:
    import fastapi

    FASTAPI_VERSION = fastapi.__version__
except ModuleNotFoundError:
    FASTAPI_VERSION = "0.70.0"


try:
    import loguru

    LOGURU_VERSION = loguru.__version__
except ModuleNotFoundError:
    LOGURU_VERSION = "0.5.3"


DYNACONF_VERSION = "3.1.7"