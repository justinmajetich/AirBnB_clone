-- Prepare a MySQL sever for the project
-- hbnb_test_db: A database
-- hbnb_test: A new user (in localhost)
-- hbnb_test_pwd: Password of the database
-- hbnb_test should have all privileges on the database 'hbnb_test_db' (and only this database)
-- hbnb_test should have SELECT privilege on the database 'performance_schema' (and only this database)
-- If the database hbnb_test_db or the uer hbnb_test already exists, this script should not fail

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

USE hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
	IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_test_db.*
	TO 'hbnb_test'@'localhost'
	WITH GRANT OPTION;

GRANT SELECT ON performance_schema.*
	TO 'hbnb_test'@'localhost'
	WITH GRANT OPTION;
