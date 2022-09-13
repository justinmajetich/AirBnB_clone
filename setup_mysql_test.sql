-- A script that prepares a test server for the MSQL server for the project

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
ALTER USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
