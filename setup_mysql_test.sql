-- create hbnb_test_db database

CREATE database IF NOT EXISTS hbnb_test_db;
-- create new user for the database test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- given priviledge
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- select priviledge to the new user on the db test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';