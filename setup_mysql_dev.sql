-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to user on database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT on performance_schema to user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush to appply changes immediately
FLUSH PRIVILEGES;
