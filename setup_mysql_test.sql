-- Create a db to test sql for the project
-- called hbnb_test_db
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Create user for the db called hbnb_test
-- Create password for the user
-- Grant privileges to the user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
