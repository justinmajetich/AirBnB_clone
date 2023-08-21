-- script that prepares a MySQL server for the project for the database hbnb_test_db
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hbnb_test_pwd';
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
