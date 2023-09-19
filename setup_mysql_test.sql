-- This Script creates a MuSQL server
-- Then Creates a DataBase -> hbnb_dev_db
-- Creates a User -> hbnb_dev in LocalHost
-- Creates a Password of hbnb_dev Set to --> hbnb_dev_pwd
-- Give SELECT Previleges to hbnb_dev on hbnb_dev_db's Performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
