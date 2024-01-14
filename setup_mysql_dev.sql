-- script that prepares a MySQL server for the project
-- crating the database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- CRATE A NEW USER IF NOT EXISTS
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- give all rpiv to the user hbnb_dev for db hbnb_dev_db
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- gice selct prev to hbnb_dev on erformance_schema
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- reloade and save
FLUSH PRIVILEGES;
