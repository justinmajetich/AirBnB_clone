A script that prepares a MySQL for the project.

CREATE USER IF NOT EXISTS
'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

GRANT SELECT
ON performanc_scheme.*
TO 'hbnb_dev'@'localhost'
WITH GRANT OPTION;

GRANT ALL PRIVILEGES
ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost'
WITH GRANT OPTION;

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
