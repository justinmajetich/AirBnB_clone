-- Creates the database hbnb_dev_db
-- Adds a new user in localhost and set new password set to hbnb_dev_pwd
-- Grant all privileges to new user on hbnb_dev_db
-- Grant select privileges on performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
DROP USER hbnb_dev@localhost;
FLUSH PRIVILEGES;
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
