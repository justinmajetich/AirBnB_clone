-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the hbnb_dev_db database to the hbnb_dev user
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema database to the hbnb_dev user
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
