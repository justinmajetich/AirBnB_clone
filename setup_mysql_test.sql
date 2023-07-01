-- script that prepares a MySQL server for the project:
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
