#!/bin/sh
export FLASK_APP=./RESTapi.py
# shellcheck disable=SC2039
# shellcheck disable=SC2046
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0
hugo new site quickstart
cd quickstart
git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
echo theme = \"ananke\" >> config.toml
hugo new posts/my-first-post.md
hugo server -D