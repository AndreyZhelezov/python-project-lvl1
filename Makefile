build: # Сборка проекта
	poetry build

publish: # Публикация пакета
	poetry publish --dry-run

package-install: # Установка пакета
	python3 -m pip install --user dist/*.whl

lint: # Тестирование качества кода
	poetry run flake8 brain_games