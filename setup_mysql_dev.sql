-- Setup SQL for the project
-- Create the main database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the main user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges on the main database to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
