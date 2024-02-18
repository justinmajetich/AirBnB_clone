-- Create hbnb_dev_db database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create hbnb_dev user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant the user all privileges on hbnb_dev_db database
-- and SELECT privilege on performance_schema database
GRANT ALL
   ON hbnb_dev_db.*
   TO 'hbnb_dev'@'localhost';
GRANT SELECT
   ON performance_schema.*
   TO 'hbnb_dev'@'localhost';
