-- A script to prepare MySQL server
-- Database Name hbnb_dev_db

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- NEW USER name: hbnb_dev with all privileges on the db hbnb_dev_db
-- USER_PW : hbnb_dev_pwd
SET GLOBAL validate_password.policy=0;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- GRANT USER'S PRIVILEGES
USE hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- GRANT SELECT PRIVILEGE TO THE USER hbnb_dev ON performance_schema
USE performance_schema;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
