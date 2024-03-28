-- Create a new databse hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new user "hbnb_tests"
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges for user 'hbnb_test'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant select privilege for user 'hbnb_test'
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;