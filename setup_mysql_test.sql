--  script that prepares a MySQL server

-- Create database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user hbnb_test with password hbnb_test_pwd
CREATE USER
IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges to hbnb_test to db hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privileges to hbnb_test to db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
