-- create a database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create a user hbnb_test in localhost with password hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges to the user hbnb_test on the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant SELECT privilege to hbnb_test on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';