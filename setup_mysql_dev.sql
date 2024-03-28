<<<<<<< HEAD
-- Prevent errors in case the database already exists by attempting to create it.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db to the users.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Ensure the user has SELECT privileges on the performance_schema database.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply the changes made by the GRANT statements
FLUSH PRIVILEGES;
=======
-- Create a new Mysql database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a new user 'hbnb_dev'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges for user 'hbnb_dev'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant select privilege for user 'hbnb_dev'
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
>>>>>>> 367dd807436d7b9dadd72aa2acc99294d2ba240f
