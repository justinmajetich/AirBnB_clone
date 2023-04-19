-- Script that prepares a MySQL server for the project
-- Create the DB hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a new user hbnb_dev in localhost snd sep pwd to hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all previleges for the user on the database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Grant selected privileges on the DB performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
