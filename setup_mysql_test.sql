-- Create database if it doesn't exist, else doesn't exit
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create user if the user test doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Give all privileges to test account.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';