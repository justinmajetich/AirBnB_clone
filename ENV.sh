#!/usr/bin/env bash

# Check if they exist
printenv | grep -E HBNB_* | wc -l

# -- Otherwise --
HBNB_ENV="dev"
# HBNB_ENV="test"

HBNB_MYSQL_USER="hbnb_dev"
# HBNB_MYSQL_USER="hbnb_test"

HBNB_MYSQL_PWD="hbnb_dev_pwd"
# HBNB_MYSQL_PWD="hbnb_test_pwd"

HBNB_MYSQL_HOST="localhost"

HBNB_MYSQL_DB="hbnb_dev_db"
# HBNB_MYSQL_DB="hbnb_test_db"

HBNB_TYPE_STORAGE="db"

# ./ENV.sh && python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
