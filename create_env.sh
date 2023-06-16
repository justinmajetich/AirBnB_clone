#!/usr/bin/bash
# Create a virtual environment for the project
# Usage: source create_env.sh
# Author: Akuya Ekorot
# Date: 2023-06-16
# Version: 1.0

# Create a virtual environment
echo 'creating virtual environment created...\n'
python3 -m venv venv
echo '✅ virtual environment created\n'

# Activate the virtual environment
echo 'activating virtual environment...\n'
source venv/bin/activate
echo '✅ virtual environment activated\n'

# Set environment variables
echo 'setting environment variables...\n'
export HBNB_ENV=$1
export HBNB_MYSQL_USER=$2
export HBNB_MYSQL_PWD=$3
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=$4
export HBNB_TYPE_STORAGE=$5
echo '✅ environment variables set\n'
