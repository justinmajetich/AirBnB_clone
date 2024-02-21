#!/bin/bash

# Function to display an error message and exit
function error_exit {
    echo "$1" 1>&2
    echo "Please run the script again and make a valid selection."
    exit 1
}

echo "Select storage type (1 for file, 2 for db):"
read STORAGE_CHOICE

case "$STORAGE_CHOICE" in
    1)
        echo "Storage type selected as file. Exiting..."
        exit 0
        ;;
    2)
        STORAGE_TYPE="db"
        ;;
    *)
        error_exit "Invalid storage type choice."
        ;;
esac

echo "Enter MySQL admin username:"
read MYSQL_ADMIN_USER

echo "Enter MySQL admin password:"
read -s MYSQL_ADMIN_PWD

echo "Select environment (1 for dev, 2 for test):"
read ENV_CHOICE

case "$ENV_CHOICE" in
    1)
        ENV="dev"
        MYSQL_USER="hbnb_dev"
        MYSQL_PWD="hbnb_dev_pwd"
        MYSQL_HOST="localhost"
        MYSQL_DB="hbnb_dev_db"
        ;;
    2)
        ENV="test"
        MYSQL_USER="hbnb_test"
        MYSQL_PWD="hbnb_test_pwd"
        MYSQL_HOST="localhost"
        MYSQL_DB="hbnb_test_db"
        ;;
    *)
        error_exit "Invalid environment choice."
        ;;
esac

# Create a virtual environment
python3 -m venv venv_$ENV || error_exit "Failed to create virtual environment."

# Install necessary packages
venv_$ENV/bin/pip install setuptools || error_exit "Failed to install setuptools."
venv_$ENV/bin/pip install -r requirements.txt || error_exit "Failed to install packages from requirements.txt."

# Set up the database
if [ "$ENV" = "dev" ]
then
    mysql -u $MYSQL_ADMIN_USER -p$MYSQL_ADMIN_PWD < setup_mysql_dev.sql || error_exit "Failed to set up dev database."
elif [ "$ENV" = "test" ]
then
    mysql -u $MYSQL_ADMIN_USER -p$MYSQL_ADMIN_PWD < setup_mysql_test.sql || error_exit "Failed to set up test database."
fi

# Set environment variables
echo "export HBNB_ENV=$ENV" >> venv_$ENV/bin/activate
echo "export HBNB_MYSQL_USER=$MYSQL_USER" >> venv_$ENV/bin/activate
echo "export HBNB_MYSQL_PWD=$MYSQL_PWD" >> venv_$ENV/bin/activate
echo "export HBNB_MYSQL_HOST=$MYSQL_HOST" >> venv_$ENV/bin/activate
echo "export HBNB_MYSQL_DB=$MYSQL_DB" >> venv_$ENV/bin/activate
echo "export HBNB_TYPE_STORAGE=$STORAGE_TYPE" >> venv_$ENV/bin/activate

echo "Environment setup complete."
echo "To activate the virtual environment, run: source venv_$ENV/bin/activate"

