-- Script prepares a MySQL server for the project.

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbhnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbhnb_dev'@'localhost';
-- FLUSH PRIVILEGES;
