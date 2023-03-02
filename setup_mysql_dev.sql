-- task 3
-- makess db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS hbnb_dev IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON *.* TO  'hbnb_dev'@'localhost' WITH GRANT OPTION
GRANT SELECT ON performance_schema.*  TO 'hbnb_dev'@'localhost';
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
