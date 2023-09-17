-- creates database 'hbnb_test_db'
-- creates the user `hbnb_test` with password `hbnb_test_pwd`, and
-- with all priviledges on database 'hbnb_test_db' and SELECT priviledge on database 'performance_schema'
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
