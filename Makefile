doc:
	@echo 'Serving doc...'
	@mkdocs serve

cover:
	@echo 'Calculating test coverage...'
	@pytest --cov=asrbench

test:
	@echo 'Testing...'
	@pytest -xv