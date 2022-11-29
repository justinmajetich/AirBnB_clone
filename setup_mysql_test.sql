-- Creat DATABASE
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- CREATE new user
CREATE USER IF NOT EXISTS 'hbnb_test'@localhost IDENTIFIED BY 'hbnb_test_pwd';
-- GIVE ALL PRIVILEGES for USER in DATABASE
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@localhost;
-- GIVE SELECT PRIVILEGES for USER in DATABASE
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@localhost;
