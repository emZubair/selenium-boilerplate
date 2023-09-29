.PHONY: help rm print-container-%

update:
	pip install pip pip-tools
	pip-compile requirements/requirements.in
	pip-sync requirements/requirements.txt



diff-run-%:
	@if git diff --name-only --diff-filter=ACMRTUXB HEAD | grep -q '\.py$$'; then \
		git diff --name-only --diff-filter=ACMRTUXB HEAD | grep '\.py$$' | xargs $*; \
	else \
		echo "No Python files have been changed"; \
	fi

sort: diff-run-isort ## Sort the imports on diff files
lint: diff-run-pylint ## run pylint on diff files
format: diff-run-black ## run black on diff files
