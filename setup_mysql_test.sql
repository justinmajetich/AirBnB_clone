-- Script to prepare a MySQL server for the project:
-- a database, hbnb_test_db
-- a new user, hbnb_test (in localhost) with password 'hbnb_test_pwd',
-- with all privileges on (and only on!) db 'hbnb_test_db'
-- with 'SELECT' privilege on (and only on!) db 'performance_schema'
-- script should not fail if db hbnb_test_db or user hbnb_test already exist

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL on hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT on performance_schema.* TO 'hbnb_test'@'localhost';
