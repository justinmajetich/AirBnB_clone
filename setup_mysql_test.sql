-- A script to prepare a MySQL for the AirBnB_clone project
-- create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create a user and grant privileges
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- Set a password for hbnb_test
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- Grant all privileges on hbnb_test_db to hbnb_test
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
-- grant SELECT privileges on performance_schema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
