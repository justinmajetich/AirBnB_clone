-- create the data base if it doesnt exit
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new use in the localhost COMMENT
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grantt the user hbnb_dev all privileges on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant all Select Privileges on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
