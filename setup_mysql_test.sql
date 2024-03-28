CREATE DATABASE IF NOT EXIST hbnb_test_db;
CREATE USER IF NOT EXIST 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd'
GRANT ALL PRIVILEGES ON *hbnb_test_db* TO 'hbnb_test'@'localhost' WITH GRANT OPTION;
GRANT PRIVILEGES SELECT ON *performance_schema* TO 'hbnb_test'@'localhost';
