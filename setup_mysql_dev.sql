-- script that prepares a MySQL server for AirBnB Console v2
-- create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create user if not exist
-- user should should be identified with password hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant hbnb_dev all previleges on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- grant select privuleges on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;