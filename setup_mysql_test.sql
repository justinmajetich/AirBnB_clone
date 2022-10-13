-- prepares a MySQL test server for the AirBnb clone
-- creates a database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create a user and grant ALL privileges
CREATE USER 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL ON hbnb_test_db.*
TO 'hbnb_test'@'localhost';
-- grant SELECT privileges
GRANT SELECT ON performance_schema.*
TO 'hbnb_test'@'localhost';
