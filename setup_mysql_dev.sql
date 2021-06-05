-- creates a MySQL database and user with password and all privileges in new db,
-- plus SELECT privileges in performance_schema
CREATE DATABASE IF NOT EXISTS 'hbnb_dev_db';
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnd_dev_pwd';
GRANT ALL ON 'hbnb_dev_db'.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON 'performance_schema'.* TO 'hbnb_dev'@'localhost';
