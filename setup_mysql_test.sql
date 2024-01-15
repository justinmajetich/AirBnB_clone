-- This script prepares a MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- The script does not fail if user or database exists
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- The user is granted all privileges on the database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- The user also gets SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
