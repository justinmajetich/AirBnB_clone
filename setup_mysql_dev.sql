-- Create the database 'hbnb_dev_db' if it does not already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Switch to the 'hbnb_dev_db' database for subsequent commands
USE hbnb_dev_db;

-- Create the user 'hbnb_dev' with the password 'hbnb_dev_pwd' if it does not already exist
-- and set the authentication method to 'mysql_native_password'
CREATE USER IF NOT EXISTS 'hbnb_dev' @'localhost' 
IDENTIFIED WITH mysql_native_password BY 'hbnb_dev_pwd';

-- Grant all privileges on the 'hbnb_dev_db' database to the 'hbnb_dev' user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev' @'localhost';

-- Grant the 'hbnb_dev' user the privilege to select from the 'performance_schema' database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev' @'localhost';

-- Refresh any changes to the privileges
FLUSH PRIVILEGES;

-- Test if the user and database are accessible
SELECT DATABASE() AS "Current Database", USER () AS "Current User";