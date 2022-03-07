-- Creates the database hbnb_test_db and the user hbnb_test
-- The hbnb_test has all privileges on hbnb_test_db with password hbnb_test_pwd
--- The hbnb_test has SELECT privilege on performance_schema with password hbnb_test_pwd
CREATE DATABASE
    IF NOT EXISTS `hbnb_test_db`;
CREATE USER
    IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES
    ON `hbnb_test_db`.*
    TO 'hbnb_test'@'localhost';
GRANT SELECT
    ON `performance_schema`.*
    TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
