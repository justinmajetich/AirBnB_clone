-- This script is used to setup the MySQL database for the 
-- development environment.

-- Create the database
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- Create the user
CREATE USER IF NOT EXISTS 'hbnb_dev' @'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant the user privileges
GRANT USAGE ON *.* TO 'hbnb_dev' @'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev' @'localhost';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev' @'localhost';

-- Flush the privileges
FLUSH PRIVILEGES;
