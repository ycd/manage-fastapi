from dynaconf import Dynaconf
from dynaconf.loaders import redis_loader


from dynaconf import Dynaconf
from pydantic import BaseSettings, Extra

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[
        "settings.toml",
    ],
    environments=True,
    lowercase_read=True,
    redis_enabled=True,
)

def dynaconf_source(source: BaseSettings) -> Dynaconf:
    with settings.fresh():
        return settings


class DynaEnabledSettings(BaseSettings):
    class Config:
        case_sensitive = False
        env_file = ".env"
        extra = Extra.allow
        smart_union = True

        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                dynaconf_source,
                init_settings,
                env_settings,
                file_secret_settings,
            )

if __name__ == "__main__":
    redis_loader.write(
        settings,
        dict(
            SECRET="redis_works",
            POSTGRES_USER="postgres",
            POSTGRES_PASSWORD="postgres",
            POSTGRES_SERVER="localhost",
            POSTGRES_DB="app",
            POSTGRES_DB_TWO="app2",
            POSTGRES_DB_THREE="app3",
            **{"dynaconf_merge": True}
        ),
    )

