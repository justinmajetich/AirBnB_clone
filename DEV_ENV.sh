#!/usr/bin/env bash

# Check if they exist
# printenv | grep -E HBNB_* | wc -l

# -- Otherwise --
export HBNB_ENV="dev";
export HBNB_MYSQL_USER="hbnb_dev";
export HBNB_MYSQL_PWD="hbnb_dev_pwd";
export HBNB_MYSQL_HOST="localhost";
export HBNB_MYSQL_DB="hbnb_dev_db";
export HBNB_TYPE_STORAGE="db";
