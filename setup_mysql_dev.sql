-- Set ALL privileges on the database `hbnb_dev_db` to the `hbnb_dev` user.
-- Set SELECT privileges on the database `performance_schema` to the `hbnb_dev` user.

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
DROP USER IF EXISTS 'hbnb_dev'@'localhost';
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
