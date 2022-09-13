-- Prepares a MySQL server for the project with:
--   A database hbnb_test_db
--   A new user hbnb_test with password hbnb_test_pwd (in localhost)
--   Grants User all privileges on the database hbnb_test_db (and only this database)
--   Grants User SELECT privilege on the database performance_schema (and only this database)

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
       IF NOT EXISTS 'hbnb_test'@'localhost'
       IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES
      ON `hbnb_test_db`.*
      TO 'hbnb_test'@'localhost'
      IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT
      ON `performance_schema`.*
      TO 'hbnb_test'@'localhost'
      IDENTIFIED BY 'hbnb_test_pwd';
FLUSH PRIVILEGES;
