-- This Script creates a MuSQL server
-- Then Creates a DataBase -> hbnb_dev_db
-- Creates a User -> hbnb_dev in LocalHost
-- Creates a Password of hbnb_dev Set to --> hbnb_dev_pwd
-- Give SELECT Previleges to hbnb_dev on hbnb_dev_db's Performance_schema

DROP DATABASE IF EXISTS hbnb_dev_db;
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
