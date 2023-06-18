-- Prepares a  MySQL server for the project, creates a database hbnb_test_db,
-- create user hbnb_test and assigns neccessary permissions to it
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* to 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
