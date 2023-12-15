-- Create hbnb_test_db database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create hbnb_test user and Grant user all privileges ON hbnb_test_db
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Show current grants
SHOW GRANTS FOR 'hbnb_test'@'localhost';
