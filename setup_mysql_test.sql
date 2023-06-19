-- Prepare a MySQL server
-- Running SQL Tests
-- Create a db to test the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- creating new user hbnb_test on db hbnb_test_db

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- granting the SELECT privilege for the user hbnb_test on the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

-- granting all privileges to new user on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
