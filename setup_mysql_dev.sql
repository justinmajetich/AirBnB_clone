-- script that creates a database hbnb_dev_db in your MySQL server
-- create a new user hbnb_dev in localhost  with pw hbnb_dev_pwd
-- all privileges on hbnb_dev_db and SELECT privileges on performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER
       IF NOT EXISTS 'hbnb_dev'@'localhost'
       IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES on hbnb_dev_db.*
       TO 'hbnb_dev'@'localhost';
GRANT SELECT on performance_schema.*
      TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
