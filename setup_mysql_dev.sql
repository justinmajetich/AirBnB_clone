-- Script to prepare the MySQL server for the project

-- Create the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- Grant Select privileges to the user in the preformance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;