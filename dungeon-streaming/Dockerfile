FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY dungeon-streaming/Pipfile dungeon-streaming/Pipfile.lock /app/

RUN pip install pipenv \
    && pipenv install --deploy --system --ignore-pipfile

COPY dungeon-streaming/entrypoint.sh /app/
RUN chmod +x entrypoint.sh

COPY . /app/

CMD ./dungeon-streaming/entrypoint.sh
