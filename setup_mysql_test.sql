-- script that prepares a MySQL server for the project
-- crating the database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- CRATE A NEW USER IF NOT EXISTS
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- give all rpiv to the user hbnb_test for db hbnb_test_db
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- gice selct prev to hbnb_test on erformance_schema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- reloade and save
FLUSH PRIVILEGES;
