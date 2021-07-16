FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY dungeon-mailing/Pipfile dungeon-mailing/Pipfile.lock /app/

RUN pip install pipenv \
    && pipenv install --deploy --system --ignore-pipfile

COPY dungeon-mailing/entrypoint.sh /app/
RUN chmod +x entrypoint.sh

COPY . /app/

CMD ./dungeon-mailing/entrypoint.sh
