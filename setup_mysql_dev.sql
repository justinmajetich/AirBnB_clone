-- creates a database for AirBnb Clone V2
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* to 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema to 'hbnb_dev'@'localhost';
