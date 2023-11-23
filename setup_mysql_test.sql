-- My SQL setup file for development stage of project
-- Requirements are:
-- creates a database called hbtn_test_db
-- creates a user called hbnb_test in localhost
-- sets the password of the hbnb_test user to hbnb_test_pwd
-- grants the user ALL privileges on the database hbnb_test_db and only this database
-- grants the user SELECT privileges on the database preformance_schema and only this database
-- if the database hbnb_test_db or user hbnb_test already exist the script should not fail
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
