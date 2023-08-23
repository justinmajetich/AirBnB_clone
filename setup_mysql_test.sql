-- a script that prepares a MySQL server for the project:

-- Create Database 'hbnb_test_db' and use it
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;

-- Creat user 'hbnb_test' with password 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grand user all privilages on database 'hbnb_test_db'
-- and the 'SELECT' privilage on database 'performance_schema'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Reload and set
FLUSH PRIVILEGES;
