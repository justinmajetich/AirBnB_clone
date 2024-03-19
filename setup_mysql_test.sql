--- Creates a MySQL server with:
-- Database
-- user hbnb_test with password hbnb_test_pwd in localhost

-- Create the hbnb_test_db database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the hbnb_test user and set the password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the hbnb_test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECt privileges on performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- flus privileges to apply changes
FLUSH PRIVILEGES
