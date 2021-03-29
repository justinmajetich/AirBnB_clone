-- Create the DB hbnb_test_db and the user hbnb_test , the passwd hbnb_test_pwd
-- grant privileges and grant select for the user hbnb_test

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES
ON hbnb_test_db.*
TO 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

GRANT SELECT
ON `performance_schema`.*
TO 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';
FLUSH PRIVILEGES;
