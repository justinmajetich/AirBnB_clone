-- Create the database if it doesn't exist
-- Create the user if it doesn't exist
-- Grant all privileges on hbnb_dev_db to hbnb_dev
-- Grant SELECT privilege on performance_schema to hbnb_dev
-- Flush privileges to apply changes

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

