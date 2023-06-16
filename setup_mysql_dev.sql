-- Prepare a MySQL sever for the project
-- hbnb_dev_db: A database
-- hbnb_dev: A new user (in localhost)
-- hbnb_dev_pwd: Password of the database
-- hbnb_dev should have all privileges on the database 'hbnb_dev_db' (and only this database)
-- hbnb_dev should have SELECT privilege on the database 'performance_schema' (and only this database)
-- If the database hbnb_dev_db or the uer hbnb_dev already exists, this script should not fail

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

USE hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
	IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.*
	TO 'hbnb_dev'@'localhost'
	WITH GRANT OPTION;

GRANT SELECT ON performance_schema.*
	TO 'hbnb_dev'@'localhost'
	WITH GRANT OPTION;
