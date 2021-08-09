-- a script that prepares a MySQL server
-- CREATE
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
DROP USER IF EXISTS 'hbnb_test'@'localhost';
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
--  ".*" grants privileges on all tables of the database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
