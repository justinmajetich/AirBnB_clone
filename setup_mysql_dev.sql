-- a script that prepares a MySQL server
-- Create
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
DROP USER IF EXISTS 'hbnb_dev'@'localhost';
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
--  ".*" grants privileges on all tables of the database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
