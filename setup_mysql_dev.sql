-- prepares a MySQL server for the project
-- hbnb_dev_db Database
-- new user hbnb_dev (in localhost)
-- The password of hbnb_dev should be set to hbnb_dev_pwd
-- hbnb_dev should have all privileges on the db hbnb_dev_db (and only this db)
-- hbnb_dev should have SELECT privilege on the db performance_schema (and only this db)
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
DROP USER IF EXISTS 'hbnb_dev'@'localhost';
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
