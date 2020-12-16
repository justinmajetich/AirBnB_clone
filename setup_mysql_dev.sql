-- sql script to create database

CREATE DATABASE If NOT EXISTS hbnb_dev_db;
DROP USER if exists 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY "hbnb_dev";
GRANT USAGE on *.* to 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
