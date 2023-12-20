-- A Script that prepares a MySQL server for the project

-- Database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- A new User
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Select Database
USE hbnb_dev_db;

-- Setting All privileges for the user
GRANT ALL PRIVILEGES ON hbnb_dev_db .* TO 'hbnb_dev'@'localhost';


GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;