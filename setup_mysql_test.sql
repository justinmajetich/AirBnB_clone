-- A script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED WITH 'hbnb_test_pwd'
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO 'hbnb_test_db'@'localhost'
GRANT SELECT ON perfomance_schema . * TO 'hbnb_test'@'localhost'
