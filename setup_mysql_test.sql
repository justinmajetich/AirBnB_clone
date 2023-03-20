-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the user on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';