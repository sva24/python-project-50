# Makefile
install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff
reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build