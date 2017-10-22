.PHONY: clean-all clean-build clean-setup clean-docker \
run-docker-redis run-flask setup test

APP_NAME=Stack Calculator
PKG_NAME=stack_calculator
TCP_PORT=5000

clean-all: clean-build clean-setup clean-docker

clean-build:
	find ./${PKG_NAME} -iname *.pyc -delete
	find ./tests -iname *.pyc -delete
	rm -rf ./tests/__pycache__

clean-setup:
	rm -rf venv

clean-docker:
	docker rm -f stack_calculator_redis

run-docker-redis:
	docker run -d \
	--rm \
	--name stack_calculator_redis \
	-p 16379:6379 \
	redis:3.0.7

run-flask: venv
	. venv/bin/activate; \
	PYTHONPATH=. FLASK_APP=${PKG_NAME} FLASK_DEBUG=1 \
	flask run -h 0.0.0.0 -p ${TCP_PORT}

run-gunicorn: venv
	. venv/bin/activate; \
	PYTHONPATH=. \
	gunicorn -k gevent -w 4 -b :5000 --timeout 180 stack_calculator:app

test: venv
	. venv/bin/activate; \
	PYTHONPATH=. \
	py.test -s ./tests

setup: venv

venv: test-requirements.txt requirements.txt
	virtualenv $@; \
	. ./$@/bin/activate; \
	pip install -r test-requirements.txt; \
	pip install -r requirements.txt
	@touch venv
