-- create mysql database hbnb_test_db if not exist
   -- create new user hbnb_test in localhost if not exist
   -- set password of user to hbnb_test_pwd
   -- grant hbnd_test all privileges on hbnd_test_db
   -- grant a SELECT privilege on database performance_schema


CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
      IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT PRIVILEGES ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
