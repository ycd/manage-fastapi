## Creating a new project with Manage FastAPI

Starting new apps works just like `startproject`, since you are familiar with that command  feel free to skip this part.

* `manage-fastapi startapp [app-name]` - Creates a new app.

Let's keep working on the project that we created in Managing Projects.

#### Let's create a new app called `v1`

```shell
manage-fastapi startapp v1

Application v1 created successfully!
```

Let's see what it created. Now we have a new folder called **v1** and another folder called **v1** under our **tests** folder. Let's see what they have.

```python
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
├── tests
│   ├── __init__.py
│   └── v1
│       ├── __init__.py
│       └── test_v1.py
└── v1
    ├── api.py
    ├── endpoints
    │   ├── endpoint.py
    │   └── __init__.py
    └── __init__.py
```

In our **`fastproject/v1`** we have new **1 directory and 4 files**, let's see what they have.

In our `endpoints` folder we are going create all the endpoints for this app, also `endpoints.py` comes with a basic Hello world router,

```python
from fastapi import APIRouter, Body, Depends

router = APIRouter()


@router.get("/")
async def hello_fastapi():
    return {"Hello":"FastAPI"}
```

In our `api.py` we are getting all endpoints together to use from our **`main.py`**,

```python
# This is an example of how you can route and you are free to change
# this will not affect your be included unless you add
# from myapp.api import api_router
# to your main.py on your project folder


from fastapi import APIRouter

from myapp.endpoints import endpoint

api_router = APIRouter()
api_router.include_router(endpoint.router, prefix="/hello", tags=["myapp"])
```
