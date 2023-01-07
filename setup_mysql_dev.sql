-- A Script that prepares a MySQL server for the project.

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* to 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;