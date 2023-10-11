-- a script that prepares a MySQL server for the project:

-- Create Database 'hbnb_dev_db' and use it
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;

-- Creat user 'hbnb_dev' with password 'hbnb_dev_pwd'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grand user all privilages on database 'hbnb_dev_db'
-- and the 'SELECT' privilage on database 'performance_schema'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Reload and set
FLUSH PRIVILEGES;
