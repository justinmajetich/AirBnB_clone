-- Creates a database hbnb_dev_db (if not exists)
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates a user hbnb_dev with password 'hbnb_dev_pwd' (if not exists)
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Gives all privileges on the database hbnb_dev_db to user hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Gives SELECT privilege on the database performance_schema to user hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- End Script that prepares a MySQL server for the project

