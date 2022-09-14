-- Creates a database called hbnb_test_db in the current MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creates the MySQL server user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grants Permissions for user hbnb_test
GRANT ALL ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
