-- A script that prepares a MySQL server for the project
/*
Database -> hbnb_dev_db
User -> hbnb_dev@localhost
Password -> hbnb_dev_pwd
Privleges -> GRANT ALL
             SELECT ON performance_schema
*/

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
