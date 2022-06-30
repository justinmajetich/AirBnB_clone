-- prepare a MySQL server by creating new user w/ specific permissions for
-- databases hbnb_test_db & performance_schema db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- running flush privileges command to ensure new privileges are put into effect
FLUSH PRIVILEGES;
