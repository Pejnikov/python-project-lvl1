build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip uninstall hexlet-code
	python3 -m pip install --user dist/*.whl

install:
	poetry install

lint:
	poetry run flake8 brain_games