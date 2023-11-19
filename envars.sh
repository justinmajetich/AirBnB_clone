#!/usr/bin/env bash

export HBNB_ENV=dev
export HBNB_MYSQL_USER="hbnb_${HBNB_ENV}"
export HBNB_MYSQL_PWD="hbnb_${HBNB_ENV}_pwd"
export HBNB_MYSQL_HOST='127.0.0.1'
export HBNB_MYSQL_DB="hbnb_${HBNB_ENV}_db"
export HBNB_TYPE_STORAGE=db
export HBNB_DB_PORT=47434


alias dc='docker-compose'
