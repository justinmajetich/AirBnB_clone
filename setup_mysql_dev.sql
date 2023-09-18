--  script that prepares a MySQL server

-- Create database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user hbnb_dev with password hbnb_dev_pwd
CREATE USER
IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges to hbnb_dev to db hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privileges to hbnb_dev to db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
