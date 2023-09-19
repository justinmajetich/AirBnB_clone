-- The script creates the hbnb_dev_db database, the hbnb_dev user with the
-- specified password, and grants the necessary privileges. If the database or
-- user already exists, it will not fail.
--   mysql -u username -p < setup_mysql_dev.sql 

-- Create the hbnb_dev_db database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the hbnb_dev user with the password hbnb_dev_pwd (if it doesn't exist)
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db to the hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to the hbnb_dev user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';