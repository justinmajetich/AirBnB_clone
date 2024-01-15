
-- Prepares a MySQL server for the project.

-- Create a database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a user if it doesn't exist, identified by a password
CREATE USER IF NOT EXISTS 'hbnb_test@localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the specified database to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test@localhost';

-- Grant SELECT privilege on the performance_schema database to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_test@localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;