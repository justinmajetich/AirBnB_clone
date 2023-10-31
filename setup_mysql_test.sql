-- Creates database hbnb_test_db and new user hbnb_test in localhost
-- Set password for user, grant all privileges on database hbnb_test_db
-- Select privileges on database performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON 'hbnb_test_db'.* TO 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON 'performance_schema'.* TO 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';
FLUSH PRIVILEGES;