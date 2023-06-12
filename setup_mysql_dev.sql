-- Creates the database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- add the user hbnb_dev identified with password 'hbnb_dev_pwd'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- add privileges to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- refresh to apply privileges
-- FLUSH PRIVILEGES;