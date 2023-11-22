--  Script sets up Mysql databases

-- create database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create a user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant permissions
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';