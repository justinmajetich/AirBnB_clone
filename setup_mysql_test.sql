-- this script prepare  Mysql test server for the project
-- create test database with name hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create a new user named hbnb_test in local host
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all priviledge on hbnb_test_db to user hbnb_tes
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- grant SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
