-- A script that prepares a MySQL server for the project
-- Create database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create User hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant User hbnb_dev, the privilege to query `performance_scheme`
-- And its tables with SELECT
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Grant User hbnb_dev, all the privileges to perform operation on
-- `hbnb_dev_db` and its tables
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost'

-- Flush privileges
FLUSH PRIVILEGES;
