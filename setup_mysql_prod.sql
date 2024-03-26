-- Create the database 'hbnb_prod_db' if it does not already exist
CREATE DATABASE IF NOT EXISTS hbnb_prod_db;

-- Switch to the 'hbnb_prod_db' database for subsequent commands
USE hbnb_prod_db;

-- Create the user 'hbnb_prod' with the password 'hbnb_prod_pwd' if it does not already exist
-- and set the authentication method to 'mysql_native_password'
CREATE USER IF NOT EXISTS 'hbnb_prod' @'localhost' IDENTIFIED
WITH
    mysql_native_password BY 'hbnb_prod_pwd';

-- Grant all privileges on the 'hbnb_prod_db' database to the 'hbnb_prod' user
GRANT ALL PRIVILEGES ON hbnb_prod_db.* TO 'hbnb_prod' @'localhost';

-- Grant the 'hbnb_prod' user the privilege to select from the 'performance_schema' database
GRANT SELECT ON performance_schema.* TO 'hbnb_prod' @'localhost';

-- Refresh any changes to the privileges
FLUSH PRIVILEGES;

-- Test if the user and database are accessible
SELECT DATABASE() AS "Current Database", USER () AS "Current User";