install:
	pipenv install

activate:
	pipenv shell

migrations: 
	docker-compose -f local.yml run --rm -w /src/backend_api web python manage.py makemigrations

migrate:
	docker-compose -f local.yml run --rm -w /src/backend_api web python manage.py migrate

test:
	docker-compose -f local.yml run --rm -w /src/backend_api web py.test $(path) $(options)

psql_shell:
	docker-compose -f local.yml run --rm postgres psql -d database -U user -W password

up:
	docker-compose -f local.yml up

down:
	docker-compose -f local.yml down

clear-docker:
	docker container prune && docker image prune -a && docker volume prune && docker network prune

rebuild: down
	docker-compose -f local.yml up --build --force-recreate --no-deps -d

superuser:
	docker-compose -f local.yml run --rm -w /src/backend_api web python manage.py createsuperuser

shell:
	docker-compose -f local.yml run --rm -w /src/backend_api web python manage.py shell

check-migrations:
	docker-compose -f local.yml run --rm -w /src/backend_api web python manage.py makemigrations --check --dry-run

named-migration:
	docker-compose -f local.yml run --rm -w /src/backend_api web python manage.py makemigrations $(app) --name $(name)

squash:
	docker-compose -f local.yml run --rm -w /src/backend_api web python manage.py squashmigrations $(app) $(min) $(max) --squashed-name $(name)

test-frontend:
	docker-compose -f local.yml run --rm client yarn test $(options)
