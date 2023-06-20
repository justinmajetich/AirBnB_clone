CREATE  USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
GRANT SELECT on performance_schema.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
