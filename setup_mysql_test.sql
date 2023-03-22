-- Prepares a MySQL server for the AirBnB clone development testing

-- Create test database
DROP DATABASE
  IF EXISTS hbnb_test_db;
CREATE DATABASE
  IF NOT EXISTS hbnb_test_db;

-- Create test user
CREATE USER
  IF NOT EXISTS 'hbnb_test'@'localhost'
  IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to test user
GRANT ALL PRIVILEGES
  ON hbnb_test_db.*
  TO 'hbnb_test'@'localhost';

GRANT SELECT
  ON performance_schema.*
  TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
