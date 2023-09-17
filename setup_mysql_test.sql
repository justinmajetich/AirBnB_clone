-- creates the database hbnb_test_db in MySQL server
-- create user hbnb_test with pwd hbnb_test_pwd
-- grant hbnb_test select on performance_schema
-- grant all privileges on hbnb_test_db
-- only if database doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
