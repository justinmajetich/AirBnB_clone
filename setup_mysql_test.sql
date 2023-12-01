-- create a database hbnb_test_db
-- create a new user hbnb_test (in localhost)
-- set password of hbnb_test to hbnb_test_pwd
-- set hbnb_test with all privileges on database hbnb_test_db only
-- set hbnb_test with SELECT privilege on the database performance_schema only

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
