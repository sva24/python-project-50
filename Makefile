# Makefile
install: #  установка poetry
	poetry install

build: # билд)
	poetry build

publish: #  отладка публикаций без добавления в каталог PyPI
	poetry publish --dry-run

package-install: # установка пакета из ОС
	python3 -m pip install --user dist/*.whl

lint: # запуск линтера
	poetry run flake8 gendiff
reinstall: # пересборка пакета
	python3 -m pip install --user --force-reinstall dist/*.whl
