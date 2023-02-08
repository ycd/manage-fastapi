<div align="center">
<h1>manage-fastapi</h1>

[manage-fastapi](https://github.com/ycd/manage-fastapi) Project generator and manager for FastAPI


![init_fastapi](assets/readme.gif)

<p align="center">
    <a href="https://github.com/ycd/manage-fastapi" target="_blank">
        <img src="https://img.shields.io/github/last-commit/ycd/manage-fastapi?style=for-the-badge" alt="Latest Commit">
    </a>
        <img src="https://img.shields.io/github/workflow/status/ycd/manage-fastapi/Test?style=for-the-badge">
        <img src="https://img.shields.io/codecov/c/github/ycd/manage-fastapi?style=for-the-badge">
    <br />
    <a href="https://pypi.org/project/manage-fastapi" target="_blank">
        <img src="https://img.shields.io/pypi/v/manage-fastapi?style=for-the-badge" alt="Package version">
    </a>
    <img src="https://img.shields.io/pypi/pyversions/manage-fastapi?style=for-the-badge">
    <img src="https://img.shields.io/github/license/ycd/manage-fastapi?style=for-the-badge">
</p>
</div>


---

**Source Code**: View it on [Github](https://github.com/ycd/manage-fastapi/)

---


##  Features 🚀

* #### Creates customizable **project boilerplate.**
* #### Creates customizable **app boilerplate.**
* #### Handles the project structuring for you.
* #### Optional Dockerfile generation.
* #### Optional docker-compose generation for your project needs.
* #### Optional pre-commit hook generation.


## Installation 📌

* Prerequisites
    * Python 3.7 +

Manage FastAPI can be installed by running

```python
pip install manage-fastapi
```


## Getting started 🎈

Easiest way to start is using the defaults:

```bash
fastapi startproject [name]
```

But there is an **interactive** mode!

```bash
fastapi startproject [name] --interactive
```



## Command line options 🧰

Manage FastAPI provides three different commands.

You can list them with

```bash
fastapi --help
```

<img src="docs/docs_assets/fastapi-help.png" width=600>

The idea is to have a highly customizable CLI, but at the same time a simple interface for new users. You can see the available options for `startproject` running `fastapi startproject --help`:

<img src="docs/docs_assets/startproject-help.png" width=600>

The other commands are already available but the current implementation is too shallow. More details about `startapp` and `run` commands will be provided once they have more functionalities, at the moment you can run `startapp` by just:

```bash
fastapi startapp {name}
```

On the other hand, the `run` command expects you to have a `startproject` structure:

```bash
fastapi run
```

## License

This project is licensed under the terms of the MIT license.
