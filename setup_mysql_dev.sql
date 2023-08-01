-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create user in localhost identified by password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges to hbnb_dev on the database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb'@'localhost';
-- Grant select privilege to hbnb_dev on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';