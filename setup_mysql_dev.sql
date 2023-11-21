-- A script that prepares a MySQL server for the project

-- Create database if it doesn't exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create User if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant User hbnb_dev, the privilege to query `performance_scheme`
-- And its tables with SELECT
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Grant User hbnb_dev, all the privileges to perform operation on
-- `hbnb_dev_db` and its tables
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost'

-- Flush privileges
FLUSH PRIVILEGES;
