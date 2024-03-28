-- Create a new database `hbnb_dev_db` and a new user `hbnb_dev`
-- Grant all Privileges to this user on the hbnb_dev_db
-- Grant SELECT privileges to this user on the performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
       IDENTIFIED BY 'hbnb_dev_pwd';
 GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
 GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
