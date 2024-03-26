-- Description: This script is used to create a test database and user for the hbnb project.

CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
CREATE USER IF NOT EXISTS `hbnb_dev`@`localhost` IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO `hbnb_dev`@`localhost`;
GRANT SELECT `performance_schema`.* TO `hbnb_dev`@`localhost`;
FLUSH PRIVILEGES;
