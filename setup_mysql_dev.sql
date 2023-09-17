-- creates database 'hbnb_dev_db'
-- creates the user `hbnb_dev` with password `hbnb_dev_pwd`, and
-- with all priviledges on database 'hbnb_dev_db' and SELECT priviledge on database 'performance_schema'
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
