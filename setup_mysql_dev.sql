-- create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create user if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant privileges to the user for the database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- grant SELECT privilege to the user for performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
