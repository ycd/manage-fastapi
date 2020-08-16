

<h3 align="center">
    <strong>Managing FastAPI projects made easy.</strong>
</h3>
<p align="center">
<img src="https://img.shields.io/github/issues/ycd/manage-fastapi?style=for-the-badge">
<a href="https://github.com/ycd/manage-fastapi" target="_blank">
    <img src="https://img.shields.io/bitbucket/pr-raw/ycd/manage-fastapi?style=for-the-badge" alt="Build">
</a>
<a href="https://github.com/ycd/manage-fastapi" target="_blank">
    <img src="https://img.shields.io/github/last-commit/ycd/manage-fastapi?style=for-the-badge" alt="Latest Commit">
</a>
<br />
<a href="https://pypi.org/project/fastapi-utils" target="_blank">
    <img src="https://img.shields.io/pypi/v/manage-fastapi?style=for-the-badge" alt="Package version">
</a>
    <img src="https://img.shields.io/pypi/pyversions/manage-fastapi?style=for-the-badge">
    <img src="https://img.shields.io/github/license/ycd/manage-fastapi?style=for-the-badge">
</p>


---

**Documentation**: View it on [website](https://ycd.github.io/manage-fastapi/)

**Source Code**: View it on [Github](https://github.com/ycd/manage-fastapi/)

**Installation**: `pip install manage-fastapi`

---



##  Features 🚀

* #### Creates customizable **project boilerplate.**
* #### Creates customizable **app boilerplate.**
* #### Handles the project structing for you.
* #### Get fancy information about your Pydantic models.



## Example folder structure 📦 
```
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

## Getting information about our Pydantic models.

```
manage-fastapi showmodels
```


## With this command we are getting a fancy output of our models.

```
╔════════════════════════════════╗
║ item.py                        ║
║ -------                        ║
║ ItemBase                       ║
║ ItemCreate                     ║
║ ItemUpdate                     ║
║ ItemInDBBase                   ║
║ Item                           ║
║ ItemInDB                       ║
╚════════════════════════════════╝
╔════════════════════════════════╗
║ token.py                       ║
║ --------                       ║
║ Token                          ║
║ TokenPayload                   ║
╚════════════════════════════════╝
```


## Installation 📌

`pip install manage-fastapi`


## License

This project is licensed under the terms of the MIT license.
