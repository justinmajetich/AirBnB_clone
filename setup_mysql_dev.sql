CREATE DATABASE IF NOT EXIST hbnb_dev_db;
CREATE USER IF NOT EXIST hbnb_dev;
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd'
GRANT PRIVILEGES ON *hbnb_dev_db* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON *performance_schema* TO 'hbnb_dec'@'localhost';
