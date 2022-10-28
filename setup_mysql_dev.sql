-- Create database hbnb_dev_db and user hbnb_dev

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL on hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT on performance_schema.* TO 'hbnb_dev'@'localhost';