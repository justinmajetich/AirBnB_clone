-- This script is used to setup the MySQL database for the 
-- test environment.

-- Create the database
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Create the user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant the user privileges
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test' @'localhost';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test' @'localhost';

-- Flush the privileges
FLUSH PRIVILEGES;
