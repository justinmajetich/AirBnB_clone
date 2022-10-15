#!/usr/bin/env bash

# Check if they exist
printenv | grep -E HBNB_* | wc -l

# -- Otherwise --
export HBNB_ENV="test"
export HBNB_MYSQL_USER="hbnb_test"
export HBNB_MYSQL_PWD="hbnb_test_pwd"
export HBNB_MYSQL_HOST="localhost"
export HBNB_MYSQL_DB="hbnb_test_db"
export HBNB_TYPE_STORAGE="db"
