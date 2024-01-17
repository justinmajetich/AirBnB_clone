-- create database if exists not failure
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create the MySQL server user hbnb_dev and grant all privileges.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY "hbnb_dev_pwd";
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- grant SELECT privilege on the performance schema table
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- reload with new privileges
FLUSH PRIVILEGES;
