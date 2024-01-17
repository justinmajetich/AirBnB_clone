-- setup_test_database.sql

-- Create the test database
CREATE DATABASE IF NOT EXISTS test_airbnb;

-- Use the test database
USE test_airbnb;

-- Create a states table for testing
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
