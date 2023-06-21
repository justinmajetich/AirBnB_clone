-- Write a script that prepares a MySQL server --
-- Create db 'hbnb_dev_db' --
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Add new user 'hbnb_dev' in localhost --
-- User 'hbnb_dev' password should be 'hbnb_dev_pwd' --
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- User 'hbnb_dev' should have SELECT privileges on db 'performance_schema' --
GRANT SELECT ON performance_schema.*
TO 'hbnb_dev'@'localhost';

-- User 'hbnb_dev' should have all privileges on db 'hbnb_dev_db' --
GRANT ALL PRIVILEGES ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
