-- Create or use hbnb_test_db database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create or replace hbnb_test user and set password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to hbnb_test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_test user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
