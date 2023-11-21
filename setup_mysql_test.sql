-- A script that prepares a MySQL server for the project
-- Create A database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create A user 'hbnb_test';
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant the user all privilege to the created database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;
