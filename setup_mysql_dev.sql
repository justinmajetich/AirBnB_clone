-- hbnb_dev_db
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev' @'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges on the hbnb_dev_db database to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev' @'localhost';
-- Grant SELECT privilege on the performance_schema database to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev' @'localhost';