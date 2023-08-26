-- creates project testing database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creates new user hbnb_test granting all privileges on the hbnb_test_db database
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grants the SELECT privileges for user hbnb_test on the performance_schema db
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- grants all privileges to the new user on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
