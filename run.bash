#!/usr/bin/env bash
HBNB_ENV=''
HBNB_TYPE_STORAGE=''
HBNB_MYSQL_USER=''
HBNB_MYSQL_HOST=''
HBNB_MYSQL_DB=''
HBNB_MYSQL_PWD=''
APP_FILE=''
APP_ARGS=()

# get the application or command to run
if [[ ${#@} -gt 0 ]]; then
    file="$1"
    if [ -x "$file" ]; then
        start_str=$(echo "$file" | cut -c -2)
        if [[ "$start_str" != "./" ]]; then
            APP_FILE='./'"$file"
        else
            APP_FILE="$file"
        fi
    else
        APP_FILE=$(echo "$file" | cut -d ' ' -f 1)
        args_str=$(echo "$file" | cut -d ' ' -f 2-)
        read -sr -a APP_ARGS < <(echo "$args_str")
    fi
else
    echo -e "\e[31mError:\e[0m No file or command provided"
    echo 'Usage: ./run.bash file|command [environment] [storage]'
    exit 1
fi

# get the application environment
if [[ ${#@} -gt 1 ]]; then
    HBNB_ENV="$2"
else
    read -p 'Environment [dev]: ' -r HBNB_ENV
    if [[ "$HBNB_ENV" == '' ]]; then
        HBNB_ENV='dev'
    fi
fi

# get the storage mechanism
if [[ ${#@} -gt 2 ]]; then
    HBNB_TYPE_STORAGE="$3"
else
    read -p 'Storage Type [db]: ' -r HBNB_TYPE_STORAGE
    if [[ "$HBNB_TYPE_STORAGE" == '' ]]; then
        HBNB_TYPE_STORAGE='db'
    fi
fi
if [[ "$HBNB_TYPE_STORAGE" == 'db' ]]; then
    read -p 'User [hbnb_dev]: ' -r HBNB_MYSQL_USER
    if [[ "$HBNB_MYSQL_USER" == '' ]]; then
        HBNB_MYSQL_USER='hbnb_dev'
    fi
    read -p 'Host [localhost]: ' -r HBNB_MYSQL_HOST
    if [[ "$HBNB_MYSQL_HOST" == '' ]]; then
        HBNB_MYSQL_HOST='localhost'
    fi
    read -p 'Database [hbnb_dev_db]: ' -r HBNB_MYSQL_DB
    if [[ "$HBNB_MYSQL_DB" == '' ]]; then
        HBNB_MYSQL_DB='hbnb_dev_db'
    fi
    read -p 'Enter DB password: ' -sr HBNB_MYSQL_PWD
fi

echo -e "Running \e[34m[$APP_FILE]\e[0m"
# shellcheck disable=SC2086
env HBNB_MYSQL_USER="$HBNB_MYSQL_USER" \
  HBNB_MYSQL_HOST="$HBNB_MYSQL_HOST" \
  HBNB_MYSQL_DB="$HBNB_MYSQL_DB" \
  HBNB_ENV="$HBNB_ENV" \
  HBNB_TYPE_STORAGE="$HBNB_TYPE_STORAGE" \
  HBNB_MYSQL_PWD="$HBNB_MYSQL_PWD" \
  "$APP_FILE" ${APP_ARGS[*]}
