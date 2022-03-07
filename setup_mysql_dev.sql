-- Creates the database hbnb_dev_db and the user hbnb_dev
-- The hbnb_dev has all privileges on hbnb_dev_db with password hbnb_dev_pwd
--- The hbnb_dev has SELECT privilege on performance_schema with password hbnb_dev_pwd
CREATE DATABASE
    IF NOT EXISTS `hbnb_dev_db`;
CREATE USER
    IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES
    ON `hbnb_dev_db`.*
    TO 'hbnb_dev'@'localhost';
GRANT SELECT
    ON `performance_schema`.*
    TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
