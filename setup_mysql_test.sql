-- Prepare a MySQL server
-- Running SQL Tests
-- Create a db to test the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges
GRANT ALL PRIVILEGES ON hbnb_test-db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

--Grant SELECT Privileges on db=performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
