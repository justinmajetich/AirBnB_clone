-- script that prepares a MySQL server for the project
-- creates a dbase
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creates user if not exists and sets a password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- gives all privileges on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Gives SELECT privilege on database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- refresh the MySQL server's privilege cache
FLUSH PRIVILEGES;
