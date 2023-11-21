-- a script that prepares for MySQL server for the project

-- create a database for the project
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- create a user for the project
CREATE USER IF NOT EXISTS 'hbnb_dev_user'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges to the new user on the project database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev_user'@'localhost';

-- SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev_user'@'localhost';

-- flush privileges
FLUSH PRIVILEGES;
