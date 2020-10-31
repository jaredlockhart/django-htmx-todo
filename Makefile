WAIT_FOR_DB = /app/bin/wait-for-it.sh db:5432 &&

COMPOSE = docker-compose -f docker-compose.yml
MIGRATE = python manage.py migrate

secretkey:
	openssl rand -hex 24

compose_build:
	$(COMPOSE)  build

compose_stop:
	$(COMPOSE) kill

compose_rm:
	$(COMPOSE) rm -f -v

volumes_rm:
	docker volume prune -f

kill: compose_stop compose_rm volumes_rm
	echo "All containers removed!"

up: compose_build
	$(COMPOSE) up

bash: compose_build
	$(COMPOSE) run app bash

refresh: kill compose_build
	$(COMPOSE) run app sh -c '$(WAIT_FOR_DB) $(MIGRATE)'