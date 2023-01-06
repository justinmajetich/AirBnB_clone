-- Prepares a MySQL server for the project AirBNB Clone by:
-- Creating a Database, hbnb_test_db
-- Creating a user, hbnb_test (in localhost) with the password: hbnb_test_pwd
-- the user should have all privileges on the database hbnb_test_db (and only this database)
-- they should also have SELECT privileges on the database performance_schema (and only this database)
-- the script should NOT fail if the database and/ user already exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db; -- create the db
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd'; -- create user
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost'; -- grant all privileges
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost'; -- grant SELECT privileges
