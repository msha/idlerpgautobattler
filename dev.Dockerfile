FROM python:3.9

WORKDIR /usr/src/game

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV development
ENV FLASK_APP src/app.py
ENV POETRY_HOME=/usr

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
RUN poetry --version

COPY pyproject.toml poetry.lock /usr/src/game/

RUN poetry install --no-interaction

EXPOSE 5000

COPY . /usr/src/game

CMD ["poetry","run","invoke","start"]