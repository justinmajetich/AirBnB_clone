-- database mysql_test
-- if database mysql_test does not exist, create it
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- user for database
-- if user already exists, continue
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges to user
-- if user already exists, continue
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- grant select privilege on the database performance_schema
-- if user already exists, continue
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
