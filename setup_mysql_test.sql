-- script that prepares MySQL server for the project
/*
Create the database if it doesn't exist
Create the user if they don't exist
Grant all privileges on the specified database to the user
Grant SELECT privilege on the performance_schema database
*/
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
