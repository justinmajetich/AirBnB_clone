-- script that prepares a MySQL server for the project

-- create database hbnb_dev_db of it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- creates the user hbnb_dev and grants all priviledges the user
-- on hbnb_dev and select privilege on performance_schema
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db. * TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';