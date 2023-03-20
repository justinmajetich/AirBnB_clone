-- prepares a MySQL server for the project
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates user if doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- Sets password for user
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- all privileges on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Flush privileges
FLUSH PRIVILEGES;
