-- Setting up a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
SELECT user, host FROM mysql.user WHERE user = 'hbnb_dev';
GRANT SELECT ON performance_schema .* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
