-- a script that prepares a test for MySQL server for the project

-- create a database for the project
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- create a user for the project
CREATE USER IF NOT EXISTS 'hbnb_test_user'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges to the new user on the project database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test_user'@'localhost';

-- SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test_user'@'localhost';

-- flush privileges
FLUSH PRIVILEGES;
