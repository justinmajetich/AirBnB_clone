-- Create firts DATABASE
-- Database hbtn_0c_0
-- create a new user

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- with full privileges on localhost
-- should have SELECT privilege on the database performance_schema

GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO `hbnb_dev`@`localhost`;
GRANT SELECT ON `performance_schema`.* TO `hbnb_dev`@`localhost`;
