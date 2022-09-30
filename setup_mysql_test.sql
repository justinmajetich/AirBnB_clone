<<<<<<< HEAD
-- A script that prepares a test MySQL server for the project

-- Create the database hbnb_test_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user hbnb_test
CREATE USER IF NOT EXISTS'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Set privileges for user hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
=======
-- Creating hbnb_test_db database
-- Privileges for new user (hbnb_test)
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
USE hbnb_test_db;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
>>>>>>> e7b73d271790dc7c5215818705e40e677a859f47
