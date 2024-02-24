-- The script prepares mysql database untilized in the project
-- generates project testing database called: hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Generate a user 'hbnb_test'with all privileges on 'hbnb_test_db'
-- Password is 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant only SELECT privileges to user 'hbnb_test' on db 'performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Granting 'hbnb_test' user all privileges on 'hbnb_test_db'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
