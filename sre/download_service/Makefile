clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +
	docker system prune

build:
	docker compose build

up: build
	docker compose up -d --force-recreate

stop:
	docker compose stop download-service

logs:
	docker compose logs -f download-service

shell:
	docker compose exec download-service /bin/sh

debug: up
	docker attach $(docker ps --filter "name=download-service" -q)

test: up
	docker compose exec download-service pytest

coverage:
	docker compose exec download-service pytest --cov --cov-report term-missing

lint:
	docker compose exec download-service pylint --ignore=laboratory app.py tests/