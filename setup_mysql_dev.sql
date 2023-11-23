-- My SQL setup file for development stage of project
-- Requirements are:
-- creates a database called hbtn_dev_db
-- creates a user called hbnb_dev in localhost
-- sets the password of the hbnb_dev user to hbnb_dev_pwd
-- grants the user ALL privileges on the database hbnb_dev_db and only this database
-- grants the user SELECT privileges on the database preformance_schema and only this database
-- if the database hbnb_dev_db or user hbnb_dev already exist the script should not fail
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
