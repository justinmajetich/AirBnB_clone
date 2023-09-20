-- This script is used to create the database and tables for the test

-- create project testing hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- creating new user named : hbnb_test with all privileges on  hbnb_test_db
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';

-- grant all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

-- granting the SELECT privilege to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;