--hbnb_dev_db database 
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
--  hbnb_dev  user in localhost 
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- password
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- all privileges to the user
USE hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performan