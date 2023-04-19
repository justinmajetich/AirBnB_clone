-- A script that prepare a MySql server for the project

-- Creating User
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnbLog#2';

-- Creating DataBase
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Granting Privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
