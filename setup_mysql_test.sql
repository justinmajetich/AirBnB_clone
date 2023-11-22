--  Script sets up Mysql databases for test

-- create database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;
-- create a user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant permissions
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';