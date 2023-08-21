-- Script that prepares a MySQL server for the project

-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if it doesn't already exist, with the specified password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant USAGE privilege to the user
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema database to the user
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- Grant all privileges on the hbnb_dev_db database to the user
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';