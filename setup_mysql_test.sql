-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to user on database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT on performance_schema to user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush to appply changes immediately
FLUSH PRIVILEGES;
