build: # Сборка проекта
	poetry build

publish: # Публикация пакета
	poetry publish --dry-run

package-install: # Установка пакета
	python3 -m pip install --user dist/*.whl

