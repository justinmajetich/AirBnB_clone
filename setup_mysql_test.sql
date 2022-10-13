-- This script prepares a MYSQL server for the project.
-- Creating testing database for project: hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creating a new user: hbnb_test (in localhost)
-- and setting the password to hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Granting all privileges on the database to user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Granting user SELECT privilege on the database performance_schema
GRANT SELECT on performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
