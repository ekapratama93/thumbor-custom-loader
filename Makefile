coverage:
	@pipenv run coverage xml --fail-under=10

unit:
	@ASYNC_TEST_TIMEOUT=10 pipenv run pytest --cov=thumbor_custom_loader tests/

.PHONY: test
test:
	@$(MAKE) unit coverage

.PHONY: lint
lint:
	@tput bold; echo "Running code style checker..."; tput sgr0; \
	PIPENV_DONT_LOAD_ENV=1 pipenv run flake8 -v
	@tput bold; echo "Running linter..."; tput sgr0; \
	PIPENV_DONT_LOAD_ENV=1 pipenv run pylint -E *.py
