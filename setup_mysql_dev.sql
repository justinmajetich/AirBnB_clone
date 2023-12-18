-- Creating a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Use the database
USE hbnb_dev_db;

-- Creating a new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all priviledges on the database
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';

-- Grant select priviledge
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';