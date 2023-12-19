-- SETTING UP THE DEV SQL PROFILE
--The script that doess the same
SET GLOBAL vaidate_password.policy = 0;
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@localhost;
FLUSH PRIVILEGES;
SET GLOBAL validate_password.policy = 1;
