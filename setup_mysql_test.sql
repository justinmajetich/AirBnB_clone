-- A script that prepares a test MySQL server for the project

-- Create the database hbnb_test_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user hbnb_test
CREATE USER IF NOT EXISTS'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Set privileges for user hbnb_test
USE hbnb_test_db;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
