-- Prepares a MySQL server


-- Create hbnb_test_db database
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Create hbnb_test user
CREATE USER IF NOT EXISTS `hbnb_test`@`localhost` IDENTIFIED BY 'hbnb_test_pwd';

-- Set hbnb_test user's privileges on hbnb_test_db database
GRANT ALL ON `hbnb_test_db`.* TO `hbnb_test`@`localhost`;

-- Set hbnb_test user's privileges on performance_schema database
GRANT SELECT ON `performance_schema`.* TO `hbnb_test`@`localhost`;


FLUSH PRIVILEGES;
