install:
	# install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	# format code
	black *.py mylib/*.py
lint:
	# flask8 or pylint
	pylint --disable=R,C *.py ./mylib
test:
	# test
	python -m pytest -vv --cov=mylib test_logic.py
build:
	# build container
deploy:
	# deploy
all: install lint test deploy