-- Creates a database called hbnb_dev_db in the current MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creates the MySQL server user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grants Permissions for user hbnb_test
GRANT ALL ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
