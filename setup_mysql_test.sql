-- A script that prepares MySQL server for the project

CREATE USER IF NOT EXISTS
'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

GRANT SELECT
ON performance_schema.*
TO 'hbnb_test'@'localhost'
WITH GRANT OPTION;

GRANT ALL PRIVILEGES
ON hbnb_test_db.*
TO 'hbnb_test'@'localhost'
WITH GRANT OPTION;

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
