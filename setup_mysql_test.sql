-- This script prepares a MySQL test server for the project

-- Create a new DB `hbnb_test_db` if it's inexistant
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new User if doesn't exist
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on `hbnb_test_db` DB to the User `hbnb_test`
GRANT ALL ON hbnb_test_db.* TO hbnb_test@localhost;

-- Grant select privileges on `performance_schema` to the User `hbnb_test`
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;