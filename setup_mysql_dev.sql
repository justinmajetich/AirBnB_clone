-- Create new database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create new user
CREATE USER IF NOT EXISTS `hbnb_dev`@`localhost` IDENTIFIED BY 'hbnb_dev_pwd';
-- Set all privilege for hbnb_dev_db
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
-- Set SELECT privilege for performance_schema DB
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
-- Save the changes
FLUSH PRIVILEGES;