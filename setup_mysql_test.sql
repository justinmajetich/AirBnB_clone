-- Set ALL privileges on the database `hbnb_dev_db` to the `hbnb_dev` user.
-- Set SELECT privileges on the database `performance_schema` to the `hbnb_dev` user.

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
DROP USER IF EXISTS 'hbnb_test'@'192.168.1.55';
CREATE USER 'hbnb_test'@'192.168.1.55' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'192.168.1.55';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'192.168.1.55';
FLUSH PRIVILEGES;
