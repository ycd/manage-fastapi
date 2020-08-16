
To start a new project with Manage FastAPI, you can use this:

* `manage-fastapi startproject [project-name]` - Create a new project.

This will create create **4 directories and 8 files** for you. Let's see what it includes, for instance i'm creating a new project called **fastproject**

```shell
manage-fastapi startproject fastproject

Project fastproject created successfully!
```

The command we ran above, created a `main.py` that will include all our external app's. A folder called **models** for our database stuff, another folder called **schemas** for our Pydantic models etc and a `settings.py` file.

```shell
fastproject/
├── __init__.py
├── main.py
├── core
│   ├── models
│   │   ├── database.py
│   │   └── __init__.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── schema.py
│   └── settings.py
└── tests
    └── __init__.py
```

Our **`main.py`** gonna be our controller. It will include all the routers other settings stuff to make our project more clean and easy to maintain.

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastproject.settings import settings
from fastproject.models.database import database

app = FastAPI(title=settings.PROJECT_NAME)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.on_event("startup")
async def connect_database():
    await database.connect()


@app.on_event("shutdown")
async def disconnect_database():
    await database.disconnect()
```

In **`settings.py`** we have the settings for all of our project, it comes with just a database settings but you can use the **`Settings`** class to include all your OAuth tokens secrets etc.

```python
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseSettings, AnyHttpUrl, HttpUrl, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "fastproject"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost",
        "http://localhost:80",
        "http://localhost:8000",
    ]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # Database Settings
    DB_SERVER: Optional[str] = ""
    DB_USER: Optional[str] = ""
    DB_PASSWORD: Optional[str] = ""
    DB_PORT: Optional[str] = ""
    DB_NAME: Optional[str] = ""
    DB_PORT: Optional[str] = ""

    # DATABASE_URL: Optional[
    #     str
    # ] = f"{DB_SERVER}://{DB_USER}:{DB_PASSWORD}@{DB_PORT}:{DB_PORT}/{DB_NAME}"


    # DATABASE_URL = "postgresql://user:passowrd@localhost:5432/DB_NAME"
    DATABASE_URL = "sqlite:///./test.db"



    class Config:
        case_sensitive = True


settings = Settings()
```

In **`models/database.py`** we create all our database stuff, If you don't need database you might want to skip this. **`database.py`** uses [**Databases**](https://github.com/encode/databases) library which is a great library to provide **Async** database support for Python.

```python
import sqlalchemy
from fastproject.settings import settings
import databases

database = databases.Database(settings.DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Put your database models here | Below

# FastAPI documentation for databases: https://fastapi.tiangolo.com/advanced/async-sql-databases/

# Put your database models here | Above


engine = sqlalchemy.create_engine(settings.DATABASE_URL)
metadata.create_all(engine)
```

Under **`schemas`** we will declare all our models. **`schemas/schema.py`** comes with a example class. Feel free to delete it if you are experienced with **FastAPI**.

```python
# For more information check Pydantic documentation = https://pydantic-docs.helpmanual.io/usage/models/
#
# Creating your custom classes
#
# class ClassName(BaseModel):
#     name: str
#     value: int
#

from pydantic import BaseModel, Field


class Model(BaseModel):
    pass
```

---
### Let's skip to the next documentation to see how we can create new apps.
---
