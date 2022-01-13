from typing import Optional



from typing import TYPE_CHECKING, Optional, Type, Union


from pydantic import AnyUrl, BaseModel
from pydantic.networks import RedisDsn

if TYPE_CHECKING:
    from pydantic.networks import Parts

from .types import PostgresDsn, SqliteUrl, MysqlDsn




class URIModel(BaseModel):
    url_type: Optional[Type[Union[PostgresDsn, SqliteUrl, MysqlDsn, RedisDsn, AnyUrl]]] = None
    port: Optional[int] = None
    name: Optional[str] = None
    scheme: Optional[str] = None
    host: Optional[str] = None
    database: Optional[str] = None
    user: Optional[str] = None
    password: Optional[str] = None

    def build(self) -> str:
        parts: Parts = self.dict(exclude={"url_type"})  # type: ignore
        parts["domain"] = parts.pop("host")  # type: ignore
        parts["path"] = parts.pop("database")  # type: ignore
        parts["port"] = str(parts.pop("port"))  # type: ignore
        outcome = self.url_type.apply_default_parts(parts)  # type: ignore
        if self.url_type is not None:
            built = self.url_type.build(
                scheme=str(self.scheme),
                user=str(outcome["user"]),
                password=str(outcome["password"]),
                host=str(outcome["domain"]),
                path=f"/{outcome['path']}",
                port=str(outcome["port"]),
            )
            return str(built)
        raise AttributeError("The URL Scheme Is Not Set")
        # self.url_type.build()
