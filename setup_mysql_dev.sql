-- create mysql database hbnb_dev_db if not exist
   -- create new user hbnb_dev in localhost if not exist
   -- set password of user to hbnb_dev_pwd
   -- grant hbnd_dev all privileges on hbnd_dev_db
   -- grant a SELECT privilege on database performance_schema


CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
ALTER USER 'hbnb_dev'@'localhost'
      IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT PRIVILEGES ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
