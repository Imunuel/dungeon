# Dungeon of Python Mailing Service

## Description
Data for email message from kafka topic and send message to email/emails from data

## Configuration
Configuration located in `envs/.env`, for examples see `envs/.env.ci`

## Installing on a local machine
This service requires python3.8 and .

## Linting

```sh
$ flake8
$ isort .
```

## Docker

### Building

```bash
$ docker-compose -f local-mailing.yml up
```

or 
```bash
$ docker-compose -f local-mailing.yml build
```
## Using
On main:
```bash
producer = Producer()
producer.send_message('topic', 'key', 'value')
```
On service:
```bash
consumer = Consumer()
consumer.read_message('topic')
```

