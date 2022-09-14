-- prepare a mysql database for the AIRBnB clone
-- create a database hbnb_dev_db
-- create a new user hbnb_dev in localhost and grant all privilege
-- hbnb_dev should have SELECT privilege on the database performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER
    IF NOT EXISTS 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES
    ON hbnb_dev.*
    TO 'hbnb_dev'@'localhost';

GRANT SELECT
    ON performance_schema.*
    TO 'hbnb_dev'@'localhost';
FLUCH PRIVILEGES;