-- prepares a MySQL server for the project
-- create database 'hbnb_test_db'
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- use database
USE hbnb_test_db;
-- create the user `hbnb_test` with password `hbnb_dev_pwd`
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges on database 'hbnb_test_db' to user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant SELECT privilege on database 'performance_schema' to user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;
