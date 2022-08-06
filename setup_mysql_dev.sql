-- Create a MySQL server
-- Database: hbnb_test_db
-- User: hbnb_test
-- Password: hbnb_test_pwd

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

FLUSH PRIVILEGES;
