-- Script that prepares a MySQL server for the project:
-- Create a database named 'hbnb_dev_db'
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a new user 'hbnb_dev' in db 'hbnb_dev_db'identified by password 'hbnb_dev_pwd'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant 'hbnb_dev' all privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Granting select privilege to 'hbnb_dev' on 'performance_schema'
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
