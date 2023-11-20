-- script that prepares a dev MySQL server for the AirBnB clone project.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- a new user hbnb_test (in localhost).
-- the password of hbnb_test should be set to hbnb_test_pwd.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
-- hbnb_test should have all privileges on the database hbnb_test_db only.
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
-- hbnb_test should have SELECT privilege on the database performance_schema.
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
