-- create a database hbnb_dev_db
-- create a new user hbnb_dev (in localhost)
-- set password of hbnb_dev to hbnb_dev_pwd
-- set hbnb_dev with all privileges on database hbnb_dev_db only
-- set hbnb_dev with SELECT privilege on the database performance_schema only

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev' @'localhost';
FLUSH PRIVILEGES;
