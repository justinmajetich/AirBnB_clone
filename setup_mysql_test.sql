-- script that prepares a MySQL server for the project:

-- creates the database 'hbnb_test_db'
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- creates user 'hbnb_test'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant priviledge on the database to the user 'hbnb_dev'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
