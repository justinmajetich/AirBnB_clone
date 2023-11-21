-- database hbnb_test_db
-- new user hbnb_test @ localhost pass hbnb_test_pwd
-- hbnb_test should have all privileges
-- hbnb_test should have SELECT privileges
-- if hbnb_test_db || hbnb_test exist, script should not fail

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

