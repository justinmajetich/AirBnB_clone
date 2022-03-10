-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
IDENTIFIED BY 'hbnb_test_pwd';

-- Grant priviledges on table
GRANT ALL PRIVILEDGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush priviledges
FLUSH PRIVILEDGES
