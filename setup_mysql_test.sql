-- 0x02. AirBnB clone - MySQL, task 4. MySQL setup test
-- configures a MySQL server for project 0x02 with the db `hbnb_test_db`
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
--       IDENTIFIED BY 'hbnb_test_pwd'; for pre-existing user creates bug:
-- ERROR 1396 (HY000): Operation CREATE USER failed for 'hbnb_test'@'localhost'
