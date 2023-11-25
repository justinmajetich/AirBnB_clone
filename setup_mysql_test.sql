-- AUTH: codenvibes
-- A script that prepares a MySQL server for the project.

-- Create or use hbnb_test_db database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create or update user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to hbnb_test user on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege to hbnb_test user on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
