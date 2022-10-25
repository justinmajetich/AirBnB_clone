--script that prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
    IDENTIFIED BY PASSWORD 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES on hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT on performance_schema.* TO 'hbnb_dev'@'localhost';
