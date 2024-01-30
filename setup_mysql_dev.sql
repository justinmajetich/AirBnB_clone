-- OUR FILE FOR PREPARING THE MYSQL SERVER FOR THE PROJECT --
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_PWD';
GRANT ALL PRIVILEGES ON hbnb_dev . * TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_scheme . * TO 'hbnb_dev'@'localhost';