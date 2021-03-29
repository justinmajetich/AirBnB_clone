-- Create the DB hbnb_dev_db and the user hbnb_dev, the passwd hbnb_dev_pwd
-- grant pivileges and grant select for the user hbnb_dev

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES
ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

GRANT SELECT
ON `performance_schema`.*
TO 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';
FLUSH PRIVILEGES;
