-- Prepares mysql server for the project

CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- Create user: hbnb_dev
-- Create passwd for user: hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant SELECT privileges for user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- Grant all privileges for user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;