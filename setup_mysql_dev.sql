-- create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges
GRANT ALL PRIVILEGES on hbnb_dev_db.*  TO 'hbnb_dev'@'localhost';

-- grant select privilege on performance schema
GRANT SELECT ON performance_shema.* TO 'hbnb_dev'@'localhost';