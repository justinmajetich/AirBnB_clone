-- Create Database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create User hbnb_test on localhost
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the user for the specified database

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema database

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';