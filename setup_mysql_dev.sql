-- A script that prepares a MySQL server for the project

-- Create the database hbnb_dev_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user hbnb_dev
CREATE USER IF NOT EXISTS'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Set privileges for user hbnb_dev
USE hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
