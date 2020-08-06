
PROJECT IS UNDER DEVELOPMENT



Command line management for FastAPI like django-admin



```python
manage-fastapi run 
manage-fastapi start-project # this will initialize a new project with some dirs etc.
```


Example structure

```python
manage-fastapi startproject [project_name}
```

```json
project/
├── main.py
├── __init__.py
└── project
    ├── database
    │   └── session.py
    ├── schemas
    │   └── schema.py
    └── settings.py
```



manage-fastapi startapi {api_name}

Expected behaviour: from startapi

Will understand the location of main.py and create a folder with the_name

```
v1
├── api.py
├── endpoints
│   └── endpoint.py
└── __init__.py
```


ready-to-code backend

```
project/
├── main.py
├── project
|   ├── __init__.py
│   ├── database
│   │   └── session.py
│   ├── schemas
│   │   └── schema.py
│   └── settings.py
└── v1
    ├── api.py
    ├── endpoints
    │   └── endpoint.py
    └── __init__.py
```

