-- Write a script that prepares a MySQL database for development

-- Create a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new user hbnh_dev (in localhost)
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';

-- Grant hbnb_dev SELECT privileges on performance_schema db
GRANT SELECT ON performance_schema.*
TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
