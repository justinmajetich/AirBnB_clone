-- Script that prepares a MySQL server
-- creating the database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE DATABASE hbnb_test_db;

-- create new user @ localhost
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;

-- Grant SELECT privileges on the performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost' ; 
FLUSH PRIVILEGES;
