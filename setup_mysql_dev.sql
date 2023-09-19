-- This script creates a MySQL server with:
--	Database = hbnb_dev_db
--	User(in localhost) = hbnb_dev
--	Password = hbnb_dev_pwd
--	Grants all privileges for hbnb_dev on hbnb_dev_db
--	Grants SELECT privileges for hbnb_dev on performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
