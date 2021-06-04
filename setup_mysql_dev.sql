-- Create database and user with privileges

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

DROP USER IF EXISTS 'hbnd_dev'@'localhost';
CREATE USER 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON 'hbnd_dev_db'.*
TO 'hbnb_dev'@'localhost';

GRANT SELECT ON 'performance_schema'.*
TO 'hbnb_dev'@'localhost';
