-- Create a new database `hbnb_test_db` and a new user `hbnb_test`
-- Grant all Privileges to this user on the hbnb_test_db
-- Grant SELECT privileges to this user on the performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
       IDENTIFIED BY 'hbnb_test_pwd';
 GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
 GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
