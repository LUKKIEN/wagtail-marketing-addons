.PHONY: dist docs

default: help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean:
	@find . -name '*.pyc' | xargs rm -f
	@find src -name '*.egg-info' | xargs rm -rf

develop: clean requirements  ## Install the development requirements

docs:  ## Create wagtail_marketing Sphinx documentation
	rm -rf site/ && mkdocs build

requirements:
	@pip install --upgrade -e .[doc,test]

qt:  ## Run the quick variant of the unit tests
	@py.test -q --reuse-db tests/ --tb=short

lint:
	@flake8 src --exclude migrations

isort:
	isort `find . -name '*.py' -not -path '*/migrations/*'`

dist: clean
	@rm -rf dist/*
	@python setup.py sdist bdist_wheel
	ls -l dist

release: dist  ## Release wagtail_marketing distribution to PyPi
	pip install twine
	twine upload -r lukkien dist/*
