-- MySQL developement Setup Script
-- Create DB
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Give user all permissions on made db
GRANT ALL ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';
-- give dev user select
GRANT SELECT ON performance_schema.*
TO 'hbnb_dev'@'localhost';
