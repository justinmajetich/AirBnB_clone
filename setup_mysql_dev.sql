-- Prepare the development database on the MySQL server
-- create the development database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- add new user and set password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant priviges to user on the new database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- grand select privilege to user on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
