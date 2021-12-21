-- script prepares a MySQL server for the project
-- DB name:hbnb_test_db
-- (1)user & (2)password(@'localhost'): (1)hbnb_test(@..), (2)hbnb_test_pwd
CREATE DATABASE IF NOT EXIST hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
	IDENTIFIED BY 'hbnb_dev_pwd';

-- (1)Granting All Privileges on hbnb_dev_db DB
-- (2) Grant Select privilege on performance_schema
GRANT ALL PRIVILEGES
	ON hbnb_test_db.*
	TO 'hbnb_test'@'localhost';

GRANT SELECT
	ON performance_schema.*
	TO 'hbnb_test'@'localhost';
