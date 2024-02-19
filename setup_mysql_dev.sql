-- prepares a MySQL server for the Airbnb webapp
-- create a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create a new user in localhost with password
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant the user all permission on the database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- grant the user SELECT privilege on database performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';