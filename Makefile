.PHONY: help rm print-container-%

update:
	pip install pip pip-tools
	pip-compile requirements/requirements.in
	pip-sync requirements/requirements.txt