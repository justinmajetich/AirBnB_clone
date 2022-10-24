-- TASK 4: MySQL setup test
-- Script that prepares a MySQL server for the
-- project by adding a database and new user for
-- use with testing.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
            IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL ON `hbnb_test_db`.*
          TO 'hbnb_test'@'localhost';

GRANT SELECT ON `performance_schema`.*
          TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;