-- prepares a MySQL server for the AirBnB clone
-- create a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create a user and grant ALL privileges
CREATE USER 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';
-- grant SELECT privileges on performance_schema
GRANT SELECT ON performance_schema.*
TO 'hbnb_dev'@'localhost';
