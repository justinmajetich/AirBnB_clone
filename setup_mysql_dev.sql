-- create a database
CREATE DATABASE if not exists hbnb_dev_db;
-- create user
CREATE USER if not exists 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- all privileges
GRANT ALL privileges on hbnb_dev_db.* to 'hbnb_dev'@'localhost';
-- select privilege
GRANT SELECT on performance_schema.* to 'hbnb_dev'@'localhost';
-- ALL PRIVILEGES
FLUSH PRIVILEGES;