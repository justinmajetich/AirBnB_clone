#!/bin/bash
-- script that prepares a MySQl server

-- creates the database if it doesn't exist
-- database hbnb_test_db
CREATE DATABASE IF NOT EXITS hbnb_test_db;
-- create the user hbnb_test if it doesn't exit
CREATE USER IF NOT EXITS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all pivileges
GRANT ALL PIVILEGES ON hbnb_dev_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
