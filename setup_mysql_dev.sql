-- prepares a MySQL server for the project:

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES O 'hbnb_dev_db'.* TO 'hbnb_dev'@'localhost';
GARNT SELECT ON 'performance_schema'.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
