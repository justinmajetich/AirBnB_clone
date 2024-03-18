-- Script that prepares a MySQL server for the project:
-- Create a database hbnb_dev_db.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a user.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Give user 'hbnb_dev' all privileges on the database hbnb_dev_db.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Give user 'hbnb_dev' SELECT privileges on the database performance_schema.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
