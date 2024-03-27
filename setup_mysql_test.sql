-- Create the database 'hbnb_test_db' if it does not already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Switch to the 'hbnb_test_db' database for subsequent commands
USE hbnb_test_db;

-- Create the user 'hbnb_test' with the password 'hbnb_test_pwd' if it does not already exist
-- and set the authentication method to 'mysql_native_password'
CREATE USER IF NOT EXISTS 'hbnb_test' @'localhost' IDENTIFIED
WITH
    mysql_native_password BY 'hbnb_test_pwd';

-- Grant all privileges on the 'hbnb_test_db' database to the 'hbnb_test' user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test' @'localhost';

-- Grant the 'hbnb_test' user the privilege to select from the 'performance_schema' database
GRANT SELECT ON performance_schema.* TO 'hbnb_test' @'localhost';

-- Refresh any changes to the privileges
FLUSH PRIVILEGES;

-- Test if the user and database are accessible
SELECT DATABASE() AS "Current Database", USER () AS "Current User";