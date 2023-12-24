all: fix lint 

SRC = src/test_task_fintech/app/
TESTS = tests/

fix:
	poetry run autoflake -r --remove-all-unused-imports --remove-unused-variables --remove-unused-variables --in-place ${SRC}	
	poetry run black ${SRC}
	poetry run isort ${SRC}
	poetry run toml-sort --in-place pyproject.toml

lint:
	poetry run flake8 --exclude __init__.py ${SRC}
	poetry run mypy ${SRC}



	