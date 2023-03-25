-- prepares a MySQL server for the project
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create user if not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges to the database `hbnb_test_db`
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Reload the grant tables
FLUSH PRIVILEGES;
