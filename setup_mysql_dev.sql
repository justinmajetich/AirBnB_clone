-- Prepares a MySQL server for the project AirBNB Clone by:
-- Creating a Database, hbnb_dev_db
-- Creating a user, hbnb_dev (in localhost) with the password: hbnb_dev_pwd
-- the user should have all privileges on the database hbnb_dev_db (and only this database)
-- they should also have SELECT privileges on the database performance_schema (and only this database)
-- the script should NOT fail if the database and/ user already exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db; -- create the db
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'; -- create user
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost'; -- grant all privileges
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'; -- grant SELECT privileges
