dc=docker compose

build:
	$(dc) build

up:
	$(dc) up -d

stop:
	$(dc) stop

down:
	$(dc) down -v --remove-orphans

shell:
	$(dc) exec app bash

prune:
	docker system prune -a

conda_create:
	conda env create -f environment.yml

conda_update:
	conda env update -f environment.yml --prune

conda_remove:
	conda remove --name es_tripadvisor_nyc --all
