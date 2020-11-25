from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_{{ cookiecutter.snake_name }}():
    return "{{ cookiecutter.name }} app created!"
