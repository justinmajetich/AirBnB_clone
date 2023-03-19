-- prepares a MySQL serever for the project
-- creates database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create a user with password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant select privileges.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
