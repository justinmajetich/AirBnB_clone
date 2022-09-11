-- prepares a MySQL test server for the AirBnb clone V2
-- creates a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create a user on the database hbnb_test_db
CREATE USER 
    IF NOT EXISTS 'hbnb_dev'@'localhost' 
    IDENTIFIED BY 'hbnb_dev_pwd';

-- grant privileges on hbnb_test_db
GRANT ALL PRIVILEGES
    ON `hbnb_test_db`.*
    TO 'hbnb_test'@'localhost'
    WITH GRANT OPTION;

-- grant SELECT privileges on the database performance_schema
GRANT SELECT
   ON `performance_schema`.*
   TO 'hbnb_test'@'localhost';