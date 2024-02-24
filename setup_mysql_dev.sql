-- Create the DATABASE if not EXISTS
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the User if not EXISTS
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all PRIVILEGES on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privileges on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';


-- Flush privileges to apply changes
FLUSH PRIVILEGES;
