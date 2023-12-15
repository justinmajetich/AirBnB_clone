-- Create hbnb_dev_db database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create hbnb_dev user and Grant user all privileges ON hbnb_dev_db
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Show current grants
SHOW GRANTS FOR 'hbnb_dev'@'localhost';