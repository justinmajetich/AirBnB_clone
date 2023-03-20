-- prepares a MySQL server for the project
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create user if not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges to the database `hbnb_dev_db`
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Reload the grant tables
FLUSH PRIVILEGES;