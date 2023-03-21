-- create database 'hbnb_dev_db'
-- create new user 'hbnb_dev' (in localhost) with password 'hbnb_dev_pwd'
-- 'hbnb_dev' should have all privileges on the database 'hbnb_dev_db'
-- 'hbnb_dev' should have SELECT privilege on the database 'performance_schema'
-- If the database hbnb_dev_db or the user 'hbnb_dev' already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS hbnb_dev@localhost;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;
ALTER USER hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';

GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
ALTER USER hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';