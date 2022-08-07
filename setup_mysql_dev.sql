-- Create a MySQL server
-- Database: hbnb_dev_db
-- User: hbnb_dev
-- Password: hbnb_dev_pwd

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
DROP USER IF EXISTS 'hbnb_dev'@'localhost';
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
