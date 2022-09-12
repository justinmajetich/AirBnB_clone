-- create the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges on the new database to the new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- grant SELECT privilege to the new user on the performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
