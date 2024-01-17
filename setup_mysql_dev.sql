-- script that prepares a MySQL server

-- create a new database hbnb_dev_db if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- use the newly created database
-- USE hbnb_dev_db;

-- Create a new user hbnb_dev (in localhost)
-- The password of hbnb_dev should be set to hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- hbnb_dev should have all privileges on the database hbnb_dev_db
-- (and only this database)
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- hbnb_dev should have SELECT privilege on the database
-- performance_schema (and only this database)
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- flush privileges, so that the privilege is effected immidiately
FLUSH PRIVILEGES;
