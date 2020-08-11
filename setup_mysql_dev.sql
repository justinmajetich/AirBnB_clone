-- Creaste database hbnb_dev_db, add new user  hbnb_dev in localhost
-- passwd of hbnb_dev is hbnb_dev_pwd. hbnb_dev all privileges on hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS'hbnb_dev'@'localhost' IDENTIFIED BY 'user_password';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema TO 'hbnb_dev'@'localhost';
