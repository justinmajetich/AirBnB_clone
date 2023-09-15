-- Script that prepares a MySQL server for the AirBnB clone project.
-- Create the hbnb_dev_db database if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new user hbnb_dev (in localhost).
-- The password of hbnb_dev should be set to hbnb_dev_pwd.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- hbnb_dev should have all privileges on the database hbnb_dev_db.
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';

-- hbnb_dev should have all privileges on the database hbnb_dev_db only.
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- hbnb_dev should have SELECT privilege on the database performance_schema.
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
