SHELL=/bin/bash

freeze:
	pip freeze > requirements.txt

run:
	python main.py

size:
	du . -h --exclude=./.git --exclude=./.env --exclude=./__pycache__ --exclude=./.vscode

fullsize:
	du . -h --exclude=./.git

reposize:
	du . -h