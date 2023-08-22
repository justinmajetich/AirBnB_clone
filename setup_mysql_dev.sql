-- create a database hbnb_dev_db if not exists
-- create a user hbnb_dev with passwordd `hbnb_dev_pwd`
-- grant hbnb_dev user select priviledge on performance_schema
-- grant all privileges on hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
