-- Write a script that prepares a MySQL server --
-- Create db 'hbnb_test_db' --
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Add new user 'hbnb_test' in localhost --
-- User 'hbnb_test' password should be 'hbnb_test_pwd' --
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- User 'hbnb_test' should have all privileges on db 'hbnb_test_db' --
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- User 'hbnb_test' should have SELECT privileges on db 'performance_schema --'
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
