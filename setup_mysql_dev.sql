-- Prepares a MySQL server for the project

-- Create the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED WITH mysql_native_password BY 'hbnb_dev_pwd';

-- Grant privileges on the database
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
