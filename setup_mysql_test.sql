-- Create a database called hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new user called hbnb_dev in localhost
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- Set password
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_test_pwd';
-- Grant all privileges to the user
USE hbnb_test_db;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;