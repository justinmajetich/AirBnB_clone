-- Create Database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create User if Not Exists and Grant Permissions
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
