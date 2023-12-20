-- a script that prepares a MySQL server for development
-- create a new database if not exists
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
-- create a new user if not exists
CREATE USER IF NOT EXISTS `hbnb_dev`@`localhost` IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all persmissions to the created user on the created database
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO `hbnb_dev`@`localhost`;
-- grant 'select' permission to the created user on a built-in
-- database as a feature that monitor MySQL server at a low level
GRANT SELECT ON `performance_schema` TO  `hbnb_dev`@`localhost`;
