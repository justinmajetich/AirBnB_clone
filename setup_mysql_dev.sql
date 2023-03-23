-- Create database if it doesn't exist, else doesn't exit
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create user if the user doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Give all privileges to dev account.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';