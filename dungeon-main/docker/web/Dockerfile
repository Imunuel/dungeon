FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /src

# Django entrypoint
COPY ./dungeon-main/docker/web/start.sh /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

# Celery-beat entrypoint
COPY ./dungeon-main/docker/web/celery/beat/start.sh /start-beat
RUN sed -i 's/\r//' /start-beat
RUN chmod +x /start-beat

# Celery worker entrypoint
COPY ./dungeon-main/docker/web/celery/worker/start.sh /start-worker
RUN sed -i 's/\r//' /start-worker
RUN chmod +x /start-worker

EXPOSE 8000

# Packages dependencies
RUN pip install pipenv
#    && apk add --virtual build-deps gcc python3-dev musl-dev jpeg-dev zlib-dev\
#    && apk add postgresql-dev \
#    && apk add postgresql-client \

# Packages
COPY dungeon-main/Pipfile ./
RUN pipenv lock && pipenv install --system --dev
