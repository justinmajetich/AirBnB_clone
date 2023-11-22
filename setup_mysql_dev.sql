-- database for the project
-- if database already exists the code would not fail
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- user for the project
-- if user already exists the code would not fail
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- granting privileges to the user
-- if user already exists the code would not fail
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- granting privileges to the user
-- if user already exists the code would not fail
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
