from enum import Enum, EnumMeta


class BaseMetadataEnum(EnumMeta):
    def __iter__(self):
        return (member[1].value for member in self.__members__.items())

    def __contains__(self, other):
        try:
            self(other)
        except ValueError:
            return False
        else:
            return True


class BaseEnum(Enum, metaclass=BaseMetadataEnum):
    """Base enum class."""


class PackageManager(BaseEnum):
    PIP = "pip"
    POETRY = "poetry"


class PythonVersion(BaseEnum):
    THREE_DOT_SIX = "3.6"
    THREE_DOT_SEV = "3.7"
    THREE_DOT_EIG = "3.8"
    THREE_DOT_NIN = "3.9"
