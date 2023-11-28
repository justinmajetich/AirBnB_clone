#!/usr/bin/python3
"""
script that prepares a MySQL server for the project
"""

# Create the database hbnb_dev_db
echo "CREATE DATABASE hbnb_dev_db;" | mysql -u root -p

# Create the user hbnb_dev
echo "CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';" | mysql -u root -p

# Grant all privileges on the database hbnb_dev_db to the user hbnb_dev
echo "GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';" | mysql -u root -p

# Grant SELECT privilege on the database performance_schema to the user hbnb_dev
echo "GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';" | mysql -u root -p
