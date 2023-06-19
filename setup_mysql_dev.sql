-- Script that prepares a MySQL server
-- creating the database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE DATABASE hbnb_dev_db;

-- create new user @ localhost
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- Grant SELECT privileges on the performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost' ; 
FLUSH PRIVILEGES;
