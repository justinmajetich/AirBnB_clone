#!/usr/bin/python3
"""Creates the Database if it doesn't exist"""
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

"""Creates new user if it doesn't exist"""
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

"""Grant all privileges to the user on hbnb_dev_db"""
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

"""Grant SELECT privilege on performance_schema to hbnb_dev"""
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

"""Flush privileges to apply changes"""
FLUSH PRIVILEGES;
