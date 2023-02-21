-- Creates database hbnb_test_db if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates user hbnb_test if it doesn't exist already
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grants all privileges to hbnb_test including the SELECT privilege
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- To ensure that changes are applied, flush priviledges
FLUSH PRIVILEGES;
--Exit the script
exit 0
