-- Write a script that prepares a MySQL server for the project:
-- Create a database hbnb_dev_db
-- Create a user hbnb_dev with password hbnb_dev_pwd
-- Grant all privileges to hbnb_dev on hbnb_dev_db
-- Grant SELECT privilege on performance_schema to hbnb_dev
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';