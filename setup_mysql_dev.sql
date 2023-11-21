-- A script that prepares a MySQL server for the project

-- Create database if it doesn't exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Set the password policy to LOW
SET GLOBAL validate_password.policy = LOW;

-- Create User if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hbnb_dev_pwd';

-- Set the password policy to default (MEDIUM)
SET GLOBAL validate_password.policy = MEDIUM;

-- Grant User hbnb_dev the ability to use any database
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';

-- Grant User hbnb_dev, permission to perform all operations on the
-- database `hbnb_dev_db` and its tables
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant User hbnb_dev, the privilege to query `performance_scheme`
-- And its tables with SELECT
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
