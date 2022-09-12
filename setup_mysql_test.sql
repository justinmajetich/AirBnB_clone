-- script that prepares a MySQL server for the project

-- create database hbnb_test_db of it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- creates the user hbnb_test and grants all priviledges the user
-- on hbnb_dev and select privilege on performance_schema
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db. * TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';