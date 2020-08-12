-- 0x02. AirBnB clone - MySQL, task 3. MySQL setup development
-- configures a MySQL server for project 0x02 with the db `hbnb_dev_db`
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
--       IDENTIFIED BY 'hbnb_dev_pwd'; for pre-existing user creates bug:
-- ERROR 1396 (HY000): Operation CREATE USER failed for 'hbnb_dev'@'localhost'
