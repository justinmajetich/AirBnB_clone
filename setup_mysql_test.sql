-- create the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges on the new database to the new user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- grant SELECT privilege to the new user on the performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
