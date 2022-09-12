-- Creates the database hbnb_dev_db with specified paramenters
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates user if doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- Sets password for user
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- Grants privileges to user on database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grants select privileges to user on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Flush privileges
FLUSH PRIVILEGES;
