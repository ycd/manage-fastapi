# Manage FastAPI Roadmap

Hi there! :wave:

The package plans are here. If you want to contribute with new ideas, or develop the ones that are listed, read our contributing guidelines! 🤓

## Checklist

### Must

* [X] License support on `startproject`.
* [X] Docker/Docker-compose support on `startproject`.
* [X] Add basic linter tools on `startproject` (flake8, mypy and isort).
* [X] Add `.pre-commit-config.yaml` on `startproject`.
* [X] Integrate databases on `startproject`.
    - [ ] SQLALchemy
        - [X] PostgreSQL
        - [ ] MySQL
        - [ ] SQLite
    - [ ] Async SQLAlchemy
        - [ ] PostgreSQL
        - [ ] MySQL
        - [ ] SQLite
    - [ ] Gino (only supports PostgreSQL)
    - [ ] Tortoise
        - [ ] PostgreSQL
        - [ ] MySQL
        - [ ] SQLite
    - [ ] MongoDB
* [ ] Different Authentication support on `startproject`.
* [X] Support `startapp` command.
    - [X] Simple app creation.
    - [ ] Append the APIRouter to the FastAPI app.
    - [ ] Add `--app-file` and `--app-variable` options on `startapp`.
* [ ] Add tests.
* [X] Fix documentation accordingly.

### Nice to have

* [ ] VSCode debugger support on `startproject` (available via docker).
* [ ] Support different CI on `startproject`.
* [ ] Add support for `hypercorn` on `run`.
* [ ] Create `migrations`/`migrate` command.
* [ ] Add `logger` to `startproject` structure.
* [ ] Base CRUD class to `startproject`.

### Additional

* [ ] Script to copy `index.md` to `README.md` and verify if they are the same.

## Questions

* Should we support .git by default?
* Should CORSMiddleware be optional?
