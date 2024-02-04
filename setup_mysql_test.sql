-- OUR FILE FOR PREPARING THE MYSQL SERVER FOR THE PROJECT --
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test . * TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_scheme . * TO 'hbnb_test'@'localhost';