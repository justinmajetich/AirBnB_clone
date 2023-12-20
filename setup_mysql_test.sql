-- Create a user hbnb_test with password hbnb_test_pwd
-- and a database hbnb_test_db
-- hbnb_test should have all privileges on the database hbnb_test_db
-- hbnb_test should have SELECT privilege on the database performance_schema
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
