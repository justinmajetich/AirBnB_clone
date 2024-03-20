-- Create or use hbnb_dev_db database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create or replace hbnb_dev_db user and set password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'
-- Grant all priviledges on hbnb_dev_db to hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
-- Grant SELECT privilege on performance_schema to hbnb_dev user
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
