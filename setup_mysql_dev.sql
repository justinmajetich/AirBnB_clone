-- Write a script that prepares a MySQL server for the project

-- create database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- A new user hbnb_dev (in localhost)
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- grant hbnb_dev all privilege on hbnb_dev_db database
GRANT ALL PRIVILEGES ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';

-- grant hbnb_dev SELECT privilege on performance_schema database
GRANT SELECT ON performance_schema.*
TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
