-- Prepares a MySQL server


-- Create hbnb_dev_db database
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- Create hbnb_dev user
CREATE USER IF NOT EXISTS `hbnb_dev`@`localhost` IDENTIFIED BY 'hbnb_dev_pwd';

-- Set hbnb_dev user's privileges on hbnb_dev_db database
GRANT ALL ON `hbnb_dev_db`.* TO `hbnb_dev`@`localhost`;

-- Set hbnb_dev user's privileges on performance_schema database
GRANT SELECT ON `performance_schema`.* TO `hbnb_dev`@`localhost`;


FLUSH PRIVILEGES;
