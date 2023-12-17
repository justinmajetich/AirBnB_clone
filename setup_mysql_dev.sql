--  prepares a MySQL server for the AirBNb project.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create or use the existing user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to the user on the specified database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
