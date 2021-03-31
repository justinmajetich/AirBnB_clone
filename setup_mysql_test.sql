-- Scripts that prepares a MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db. * to 'hbnb_dev'@'localhost';
GRANT SELECT performance. * TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
