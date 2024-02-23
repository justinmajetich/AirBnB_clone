--Module for  creating database and users
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'hbnb_dev'@'hbnb_test_db';
GRANT SELECT ON *.* TO 'hbnb_dev'@'performance_schema';
