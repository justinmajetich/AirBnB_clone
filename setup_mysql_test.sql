-- prepare a MySQL test server for the AirBnB clone
-- creates a database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create new user with password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.*
TO 'hbnb_test'@'localhost';
-- grant select privileges
GRANT SELECT ON perfomance_schema.*
TO 'hbnb_test'@'localhost';
