-- SQL DB creation script - creates the hbnb_dev_db database, and hbnb_dev, the superuser of that DB.

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.*  TO 'hbnb_dev'@'localhost';
GRANT SELECT ON perfomance_schema.* TO 'hbnb_dev'@'localhost';
