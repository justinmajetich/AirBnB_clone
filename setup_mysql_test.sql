-- create the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create test user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
--grant select privilege on performace schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';