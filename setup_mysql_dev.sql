-- Creates a MySql server with
-- database: hbnb_dev_db
-- user: hbnb_dev (localhost)
-- hbnb_dev pw is: hbnb_dev_pwd

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

USE hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
