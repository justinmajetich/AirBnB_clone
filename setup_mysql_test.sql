-- create a database called hbnb_test_db
-- create a new user hbnb_test in localhost with pw hbnb_test_pwd
-- all privileges on hbnb_test_db and SELECT privileges on performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
       IF NOT EXISTS 'hbnb_test'@'localhost'
       IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES on hbnb_test_db.*
      TO 'hbnb_test'@'localhost';
GRANT SELECT on performance_schema.*
      TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
