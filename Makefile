makeFileDir := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))


run:
	python3 client.py

env:
	python3 -m venv env
	source env/bin/activate

activate:
	source .venv/bin/activate

freeze:
	pip3 freeze > requirements.txt


.PHONY: run, env, activate, freeze