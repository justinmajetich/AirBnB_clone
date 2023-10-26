-- The script will create the database, user, and grant the necessary
-- privileges as specified in the SQL statements, and it won't fail if
-- the database or user already exists.
--    mysql -u username -p < setup_mysql_test.sql

-- Create the hbnb_test_db database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the hbnb_test user with the password hbnb_test_pwd (if it doesn't exist)
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to the hbnb_test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to the hbnb_test user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';