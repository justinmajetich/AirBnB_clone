-- create a database hbnb_test_db if not exists
-- create a user hbnb_test with password `hbnb_test_pwd`
-- grant hbnb_test all privileges on hbnb_test_db
-- grant hbnb_test select priviledge on performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
