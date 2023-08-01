-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create user in localhost identified by password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges to hbnb_dev on the database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant select privilege to hbnb_dev on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';