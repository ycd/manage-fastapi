


from typing import Any, Protocol, TYPE_CHECKING


from pydantic import AnyUrl
from pydantic.networks import PostgresDsn as _PostgresDsn

if TYPE_CHECKING:
    from pydantic.networks import Parts



class SqliteUrl(AnyUrl):
    allowed_schemes = {"sqlite"}
    host_required = False
    hidden_parts = {"port"}

    @staticmethod
    def get_default_parts(parts: "Parts") -> "Parts":
        {}
        return {
            "domain": "",
            "port": "" if parts["port"] in ["80", None] else parts["port"],
            "path": ":memory:",
        }

class MysqlDsn(AnyUrl):
    allowed_schemes = {"mysql", "mysql+mysqldb", "mysql+pymysql"}
    user_required = True

    @staticmethod
    def get_default_parts(parts: "Parts") -> "Parts":
        {}
        return {
            "domain": "",
            "port": "" if parts["port"] in ["80", None] else parts["port"],
            "path": "app" if parts["path"] in ["", None] else parts["path"],
        }


# A Postgresql AnyURL with default parts for localhost
class PostgresDsn(_PostgresDsn):
    @staticmethod
    def get_default_parts(parts: "Parts") -> "Parts":
        return {
            "domain": "localhost" if parts["domain"] in ["", None] else parts["domain"],
            "port": "5432",
            "path": "app" if parts["path"] in ["", None] else parts["path"],
        }


# -----------------------------------------------------------------------------
#                               Protocols
# -----------------------------------------------------------------------------
class SessionKeep(Protocol):
    def instance(self):
        pass

    # @abc.abstractmethod
    def update(self, data: Any):
        raise NotImplementedError
