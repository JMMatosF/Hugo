#!/bin/shcria_post
export FLASK_APP=./RESTapi.py
# shellcheck disable=SC2039
# shellcheck disable=SC2046
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0