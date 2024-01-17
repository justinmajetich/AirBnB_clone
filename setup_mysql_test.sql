-- create database if exists not failure
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create the MySQL server user hbnb_test and grant all privileges.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY "hbnb_test_pwd";
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- grant SELECT privilege on the performance schema table
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';


-- reload with new privileges
FLUSH PRIVILEGES;
