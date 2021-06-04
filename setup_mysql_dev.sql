-- Create database and user with privileges

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON *.*
TO 'hbnb_dev'@'localhost';

GRANT SELECT ON performance_schema.*
TO 'hbnb_dev'@'localhost';
