-- script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED  BY 'hbnb_dev';
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on hbnb_dev_db.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
GRANT SELECT on performance_schema.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
/* GRANT PRIVILEGE ON database.table TO 'hbnb_dev'@'host'; */