# Dungeon of Python

Once Upon a Time....

## Configuration
Configuration located in `envs/.env`, for examples see `envs/.env.ci`

## Installing on a local machine
This project requires python3.8 and .

Install requirements:

```sh
$ pip install pipenv
$ pipenv shell
$ pipenv install
```

```sh
$ python ./backend_api/manage.py migrate
$ python ./backend_api/manage.py createsuperuser
```

Testing:
```bash
# run unit tests
$ cd backend_api && py.test -vv
```

Development servers:

```bash
# run django dev server
$ python ./backend_api/manage.py runserver
```

## Linting

```sh
$ flake8
$ isort .
```

## Docker

### Containers management

#### Formatted output
```shell
$ docker ps -a --format "{{.ID}}: {{.Image}} {{.Names}} {{.Size}}"
```
### Building

```bash
$ docker-compose -f local.yml up
```

or 
```bash
$ docker-compose -f local.yml build ...
```
if u wanna rebuild specific container.

### Management

Basic usage of compose file:

#### Testing
```bash
$ docker-compose -f local.yml run --rm -w /src/backend_api web pytest -vv 
```

#### psql shell

```bash
$ docker-compose -f local.yml run --rm postgres psql -d database -U user -W password
```

#### Migrations

```bash
$ docker-compose -f local.yml run --rm -w /src/backend_api web python manage.py makemigrations 
$ docker-compose -f local.yml run --rm -w /src/backend_api web python manage.py migrate
```

#### Check migrations

```shell
$ docker-compose -f local.yml run --rm -w /src/backend_api web python manage.py makemigrations --check --dry-run
```
