-- script that prepares a MySQL server
-- create project developement database
--databasename : hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create new user 
--username hbnb_dev with all privileges
--password : hbnb_dev_pwd if it dosen't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--grant  all privileges to new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
--grant the SELECT privilege for user hbnb_dev in db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
