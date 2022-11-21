-- Creat DATABASE
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- CREATE new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@localhost IDENTIFIED BY 'hbnb_dev_pwd';
-- GIVE ALL PRIVILEGES for USER in DATABASE
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@localhost;
-- GIVE SELECT PRIVILEGES for USER in DATABASE
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@localhost;
