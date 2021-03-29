-- Creates database hbnb_test_db
-- Creates new user hbnb_test and sets the password
-- Sets privileges for hbnb_test on hbnb_test_db
-- Sets select privileges for hbnb_test on performance_schema
-- Flush privileges
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
