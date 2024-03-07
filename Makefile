install:
	poetry install

lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest

check:
	pytest lint

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
