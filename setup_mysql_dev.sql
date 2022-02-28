-- write a script that cretes database, adds user and sets privs
USE mysql;
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'hbnb_dev'@'hbnb_dev_db';
GRANT SELECT PRIVILEGES ON *.* TO 'hbnb_dev'@'performance_schema';
