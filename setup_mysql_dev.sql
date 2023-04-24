-- Creates database hbnb_dev_db, user hbnb_dev and grants priveleges

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
