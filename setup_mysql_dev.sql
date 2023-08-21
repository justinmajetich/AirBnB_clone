-- Create database hbnb_dev_db in user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hbnb_dev_pwd';
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
