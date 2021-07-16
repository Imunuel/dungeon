FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY dungeon-auth/Pipfile dungeon-auth/Pipfile.lock /app/

RUN pip install pipenv \
    && pipenv install --deploy --system --ignore-pipfile

COPY dungeon-auth/entrypoint.sh /app/
RUN chmod +x entrypoint.sh

COPY . /app/

CMD ./dungeon-auth/entrypoint.sh
