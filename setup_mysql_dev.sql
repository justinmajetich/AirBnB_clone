-- A script that prepares a MySQL server for the AirBnB_clone project

-- Create a database `hbnb_dev_db` for the project
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
-- Create a user and set password for the user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant the user all privileges on the database `hbnb_dev_db`
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant the user SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Flush privileges
FLUSH PRIVILEGES;
