-- create test db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges
GRANT ALL PRIVILEGES on hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant select privilege on performance_schema
GRANT SELECT PRIVILEGES ON performance_schema.* TO 'hbnb_test'@'localhost';