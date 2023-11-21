-- Script that prepares a test MySQL server for the AirBnB clone project.
-- Create the hbnb_test_db database if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user hbnb_test (in localhost).
-- The password of hbnb_test should be set to hbnb_test_pwd.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant USAGE privilege on all databases to the hbnb_test user.
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';

-- hbnb_test should have all privileges on the database hbnb_test_db only.
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- hbnb_test should have SELECT privilege on the database performance_schema.
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';