FROM tiangolo/uvicorn-gunicorn-fastapi:python{{ cookiecutter.python }}

ENV PYTHONPATH "${PYTHONPATH}:/"
ENV PORT=8000
{% if cookiecutter.packaging == "poetry" %}
# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install --no-root --no-dev
{% else %}
RUN pip install --upgrade pip

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt
{% endif %}
COPY ./app /app
