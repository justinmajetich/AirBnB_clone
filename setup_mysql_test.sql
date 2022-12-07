-- Create new database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create new user
CREATE USER IF NOT EXISTS `hbnb_test`@`localhost` IDENTIFIED BY 'hbnb_test_pwd';
-- Set all privilege for hbnb_test_db
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
-- Set SELECT privilege for performance_schema DB
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
-- Save the changes
FLUSH PRIVILEGES;