-- this creates prepares upp the mysql server up and running
-- by creating the database, user and adding priviledges.

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- hbnb_test  username with all privileges on the db hbnb_test_d
-- hbnb_test_pwd as password if it dosen't exist

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- granting the SELECT privilege for usr on the db performance_schema

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- granting all privileges to the new user on hbnb_test_db

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;