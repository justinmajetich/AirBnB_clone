-- script that prepares a MySQL server for the project:
-- database name: hbnb_test_db
-- new username: hbnb_test 
-- password of hbnb_test: hbnb_test_pwd
-- hbnb_test  has all privileges on the database hbnb_test_db
-- hbnb_test has SELECT privilege on the database performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
