-- A Script that prepares a test MySQL server for AirBnB project

-- Creating a Database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- New user to manage our database
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Setting All privileges for the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grants Select privileges to user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Clears the Grant Tables
FLUSH PRIVILEGES;