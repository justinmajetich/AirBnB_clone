--This script prepares a MYSQL server for the project.
--Creating project database: hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
--Creating a new use: hbnb_dev (in localhost)
--and setting the password to hbnb_dev_pwd
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--Granting all privileges on the database to user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
--Granting user SELECT privilege on the database performance_schema
GRANT SELECT on performance.schema TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
