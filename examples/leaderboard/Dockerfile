FROM python:3.9-slim

RUN pip install --upgrade pip 

COPY ./requirements.txt /app/

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r app/requirements.txt

COPY ./app . 