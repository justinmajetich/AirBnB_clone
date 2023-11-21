A script that prepares a MySQL for the project.

CREATE USER IF NOT EXISTS
'hbnb_dev'@'localhost'
IDENTIFIED BY hbnb_dev_pwd
IDENTIFIED BY 'hbnb_dev_pwd

GRANT SELECT
ON performanc_scheme.*
TO 'hbnb_dev'0'localhost
WITH GRANT OPTION;

GRANT SELECT
ON privrleges
TO 'hbnb_dev'@'localhost
WITH GRANT OPTION

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
