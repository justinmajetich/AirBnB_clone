-- Script that prepares a MySQL server for the project
-- Create the DB hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new user hbnb_test in localhost snd sep pwd to hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all previleges for the user on the database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Grant selected privileges on the DB performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
