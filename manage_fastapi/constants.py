from enum import Enum, EnumMeta


class BaseMetadataEnum(EnumMeta):
    def __getitem__(self, key):
        return getattr(self, key.upper())

    def __iter__(self):
        return (member[1].value for member in self.__members__.items())


class BaseEnum(Enum, metaclass=BaseMetadataEnum):
    """Base enum class."""


class Packaging(BaseEnum):
    PIP = "📃 pip"
    POETRY = "🧾 poetry"


PYTHON_VERSIONS = ("3.6", "3.7", "3.8", "3.9")
