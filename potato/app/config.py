from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, validator, AnyHttpUrl

from .types import SqliteUrl, PostgresDsn, MysqlDsn
from .actions import build_connection_string
from .dynos import DynaEnabledSettings




class Settings(DynaEnabledSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    
    PORT: int
    NAME: str
    SCHEME: str
    HOST: str
    DATABASE: str
    USER: str
    PASSWORD: str

    DATABASE_URI: Union[SqliteUrl, PostgresDsn, MysqlDsn, AnyUrl, str, None] = None

    @validator("DATABASE_URI", pre=True)
    def generate_url(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        lower_values = {k.lower(): v for k, v in values.items()}
        scheme = lower_values.pop("scheme")
        conn_str = build_connection_string(scheme, lower_values)
        return conn_str




settings = Settings()
