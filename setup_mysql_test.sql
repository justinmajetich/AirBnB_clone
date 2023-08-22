-- This script prepares mysql database that will be used for this project
-- Creates project testing database named: hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creating a user named 'hbnb_test'with all privileges on 'hbnb_test_db'
-- Password for this user is 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Granting only SELECT privilege to user 'hbnb_test' on db 'performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Granting 'hbnb_test' user all privileges on 'hbnb_test_db'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
