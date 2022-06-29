-- prepare a MySQL server by creating new user w/ specific permissions for
-- databases hbnb_test_db & performance_schema which we create
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- running flush privileges command to ensure new privileges are put into effect
FLUSH PRIVILEGES;
