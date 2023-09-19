-- Create a test database
-- This script prepares a DBMS for the airbnb project clone
CREATE IF NOT EXIST DATABASE hbnb_test_db;
CREATE IF NOT EXITS USER 'hbnb_test'@'localhost' IDENTIFIED WITH authentication_plugin BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON 'hbnb_test_db'.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON 'performance_schema'.* TO 'hbnb_test'@'localhost';
