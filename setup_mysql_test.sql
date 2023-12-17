-- A script that prepares a MySQL server for test on AirBnB_clone project

-- Create a database `hbnb_test_db` for the project
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;
-- Create a user and set password for the user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant the user all privileges on the database `hbnb_test_db`
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant the user SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Flush privileges
FLUSH PRIVILEGES;
