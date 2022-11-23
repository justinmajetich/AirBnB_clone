-- set up the databae
-- and users for th hbnb project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema. * TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;