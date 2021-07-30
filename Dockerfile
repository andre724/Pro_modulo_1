#sintax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY Pipfile Pipfile
RUN pip3 intall -r Pipfile

CMD ["python", "main.py"]






