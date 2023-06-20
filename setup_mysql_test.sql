-- Prepares a MySQL server for AirBnB Clone - MySQL project
-- Create  a database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create User hbnb_test in localhost
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges on database hbnb_test_db to User hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant select privilege on database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
