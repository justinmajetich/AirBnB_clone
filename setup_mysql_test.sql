-- script that does a mysql setup test
-- create a dbase
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creates user if not exists in localhost and sets a password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- give all privileges only on the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Gives SELECT privilege only on database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- refresh the MySQL server's privilege cache
FLUSH PRIVILEGES;
