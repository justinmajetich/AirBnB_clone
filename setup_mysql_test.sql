-- prepares a MySQL server for the project
-- create database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create new user for hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- set password for user hbnb_test
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- grant all privileges for user
GRANT ALL PRIVILEGES ON hbnb_test_db.* 	TO 'hbnb_test'@'localhost';
-- SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- flush privilaeges
FLUSH PRIVILEGES;
