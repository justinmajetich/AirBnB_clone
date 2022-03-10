-- Create the database and user for the development environment.
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- Create the user for the development environment.
CREATE USER 'hbnb_dev_user'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant the user the permissions to the database.
GRANT ALL ON `hbnb_dev_db`.* TO 'hbnb_dev_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev_user'@'localhost';

-- Flush the privileges.
FLUSH PRIVILEGES;
