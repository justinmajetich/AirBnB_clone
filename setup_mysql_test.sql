-- Create and use hbnb_test_db database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Switch to hbnb_test_db database
USE hbnb_test_db;

-- Create user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant usage on hbnb_test_db to hbnb_test
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
-- Grant Select previledges on performance_schema to hbnb_test
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
-- Grant all previledges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';