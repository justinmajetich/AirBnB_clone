-- Creating a database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Use the database
USE hbnb_test_db;

-- Creating a new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all priviledges on the database
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO 'hbnb_test'@'localhost';

-- Grant select priviledge
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';