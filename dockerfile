FROM python:3.11-slim
WORKDIR /code

RUN pip install --upgrade pip \
    && pip install poetry
COPY . /code/
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-cache --no-ansi --without dev --no-root
EXPOSE 8000
