--sql script to create database
CREATE DATABASE IF NOT EXIST hbnb_dev_db
CREATE USER IF NOT EXIST 'hbnb_dev'@'localhost' IDENTIFIED BY "hbnb_dev"
GRANT ALL ON hbnb_dev_db TO 'hbnb_dev'@'localhost'
GRANT SELECT ON performance_schema TO 'hbnb_dev'@'localhost'

