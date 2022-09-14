makeFileDir := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))


run:
	python3 client.py

env_unix:
	python3 -m venv env
	source env/bin/activate

env_activate:
	source env/bin/activate

freeze:
	pip3 freeze > requirements.txt


.PHONY: run, env_unix, env_activate, freeze