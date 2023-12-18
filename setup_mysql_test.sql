-- Script that prepares a MySQL server for the project.
-- This script is meant to be run once, before the first test is run.
-- It creates a database and a user for the project.
-- It also grants the user all privileges on the database.
-- The script assumes that the MySQL server is running on localhost.
-- The script assumes that the MySQL server is running on port 3306.
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;
SET GLOBAL validate_password.policy=0;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
USE performance_schema;
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;