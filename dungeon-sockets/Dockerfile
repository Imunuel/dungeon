FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY dungeon-sockets/Pipfile dungeon-sockets/Pipfile.lock /app/

RUN pip install pipenv \
    && pipenv install --deploy --system --ignore-pipfile

COPY dungeon-sockets/entrypoint.sh /app/
RUN chmod +x entrypoint.sh

COPY . /app/

CMD ./dungeon-sockets/entrypoint.sh
