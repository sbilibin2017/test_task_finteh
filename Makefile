all: fix lint dp dbd dubd dbp dubp ddd ddp

# SRC = src/test_task_fintech/app/
# TESTS = tests/


fix:
	poetry run autoflake -r --remove-all-unused-imports --remove-unused-variables --remove-unused-variables --in-place ${SRC}	
	poetry run black ${SRC}
	poetry run isort ${SRC}
	poetry run toml-sort --in-place pyproject.toml

lint:
	poetry run flake8 --exclude __init__.py ${SRC}
	poetry run mypy ${SRC}

dp:
	docker container prune -f
	docker volume prune -f
	docker volume rm test_task_fintech_db_data
	docker volume rm test_task_fintech_cache_data	

dbd:
	docker compose -f docker-compose.dev.yaml --env-file .env.dev build
	
dubd:
	docker compose -f docker-compose.dev.yaml --env-file .env.dev up --build

ddd:
	docker compose -f docker-compose.dev.yaml --env-file .env.dev down

dbp:
	docker compose -f docker-compose.prod.yaml --env-file .env.prod build

dubp:
	docker compose -f docker-compose.prod.yaml --env-file .env.prod up --build

ddp:
	docker compose -f docker-compose.prod.yaml --env-file .env.prod down


	