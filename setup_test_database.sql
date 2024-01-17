-- setup_test_database.sql

-- Create the test database
CREATE DATABASE IF NOT EXISTS test_airbnb;

-- Create the test user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Create a states table for testing
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Give Privileges
GRANT ALL PRIVILEGES ON test_airbnb . * TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';
