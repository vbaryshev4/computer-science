build:
	pip3 install -r requirements.txt

run:
	python3 app/__init__.py

test:
	python3 app/test_runner.py