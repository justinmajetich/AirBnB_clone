-- Wrtie a script that prepares a MySQL database for testing

-- Create a database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user hbnh_test (in localhost)
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.*
TO 'hbnb_test'@'localhost';

-- Grant hbnb_test SELECT privileges on performance_schema db
GRANT SELECT ON performance_schema.*
TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
