-- Create the database if it doesnt exits
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user hbnb_test with specified password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all priviledges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on perfomance_schema to hbnb_test
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply changes 
FLUSH PRIVILEGES;
