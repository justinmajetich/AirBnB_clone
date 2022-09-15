--  prepares a MYSQL server for Airbnb
-- sets up database
-- creates new user 
-- grants permissions

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev' @'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

GRANT SELECT ON perforance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
