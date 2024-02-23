-- Create Database for the AirBnB Project
-- Requirements - Database name: hbnb_dev_db
-- New User - hbnb_dev (in LocalHost)
-- New User PSWD - hbnb_dev_pwd
-- hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
-- If the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail

-- Create Database (If it doesn't exist)
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create User (if not one)
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Set the database.
USE hbnb_dev_db;
-- Grant the user privileges to our DB only. 
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Update the user privileges.
FLUSH PRIVILEGES;
