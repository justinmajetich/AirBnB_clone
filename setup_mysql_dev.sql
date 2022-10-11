-- A script to prepare a MySQL for the AirBnB_clone project
-- create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create a user and grant privileges
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- Set a password for hbnb_dev
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- Grant all privileges on hbnb_dev_db to hbnb_dev
-- GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
-- grant SELECT privileges on performance_schema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
