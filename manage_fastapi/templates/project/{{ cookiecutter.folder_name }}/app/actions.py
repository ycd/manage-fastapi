from .models import URIModel
from .types import PostgresDsn, SqliteUrl, MysqlDsn


def select_uri(scheme: str) -> URIModel:
    return {
        "sqlite": SqliteUrl,
        "postgresql": PostgresDsn,
        "mysql": MysqlDsn,
    }[scheme]


def build_connection_string(scheme: str, data: dict) -> str:
    uri_model = URIModel(url_type=select_uri(scheme), scheme=scheme, **data)
    built = uri_model.build()
    return built
