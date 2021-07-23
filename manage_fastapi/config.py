import os

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "templates")

try:
    import fastapi

    FASTAPI_VERSION = fastapi.__version__
except ModuleNotFoundError:
    FASTAPI_VERSION = "0.67.0"
