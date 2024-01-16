#!/bin/bash
-- script that prepares a MySQl server

-- creates the database if it doesn't exist
CREATE DATABASE IF NOT EXITS hbnb_dev_db;
-- create the user if it doesn't exit
CREATE USER IF NOT EXITS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all pivileges 
GRANT ALL PIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
