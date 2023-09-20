-- A script that prepares a MySQL server for the project.
-- Creates a database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates a new user hbnb_test (in localhost)
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Set all privileges on the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_test'@'localhost';
-- Set SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
