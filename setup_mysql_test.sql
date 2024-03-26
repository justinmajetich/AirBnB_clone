#!/bin/bash

# MySQL credentials
MYSQL_USER="root"
MYSQL_PASSWORD="your_mysql_root_password"

# Database and user details
DB_NAME="hbnb_test_db"
DB_USER="hbnb_test"
DB_PASSWORD="hbnb_test_pwd"

# Create the database if it doesn't exist
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"

# Create the user if it doesn't exist
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "CREATE USER IF NOT EXISTS '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASSWORD';"

# Grant privileges
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_USER'@'localhost';"
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "GRANT SELECT ON performance_schema.* TO '$DB_USER'@'localhost';"
