-- prepares a MySQL server for the project
-- create database 'hbnb_dev_db'
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- use database
USE hbnb_dev_db;
-- create the user `hbnb_dev` with password `hbnb_dev_pwd`
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges on database 'hbnb_dev_db' to user
GRANT ALL PRIVILEGES ON hbnb_dev_db TO 'hbnb_dev'@'localhost';
-- grant SELECT privilege on database 'performance_schema' to user
GRANT SELECT ON performance_schema TO 'hbnb_dev'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;
