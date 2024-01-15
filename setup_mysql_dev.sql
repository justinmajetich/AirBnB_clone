--create database, user and grant privileges
--create database if it doesnt exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
--create a user if not exist already
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--grant usage access to newly created user
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
