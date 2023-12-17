-- This script prepares a MySQL server for the project

-- Create a new DB `hbnb_dev_db` if it's inexistant
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new User if doesn't exist
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on `hbnb_dev_db` DB to the User `hbnb_dev`
GRANT ALL ON hbnb_dev_db.* TO hbnb_dev@localhost;

-- Grant select privileges on `performance_schema` to the User `hbnb_dev`
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;