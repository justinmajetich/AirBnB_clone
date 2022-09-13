-- Prepares a MySQL server for the project with:
--   A database hbnb_dev_db
--   A new user hbnb_dev with password hbnb_dev_pwd (in localhost)
--   Grants User all privileges on the database hbnb_dev_db (and only this database)
--   Grants User SELECT privilege on the database performance_schema (and only this database)

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER 
       IF NOT EXISTS 'hbnb_dev'@'localhost'
       IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES 
      ON `hbnb_dev_db`.*
      TO 'hbnb_dev'@'localhost'
      IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT
      ON `performance_schema`.*
      TO 'hbnb_dev'@'localhost'
      IDENTIFIED BY 'hbnb_dev_pwd';
FLUSH PRIVILEGES;
