-- script that prepares a MySQL server for the project if it does not already exist
-- database hbnb_test_db
CREATE database IF NOT EXISTS hbnb_test_db;

-- creates new user hbnb_test  (in localhost)
-- password of hbnb_test  should be set to hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test '@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
ALTER USER IF EXISTS 'hbnb_test '@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- hbnb_test  should have all privileges on the database hbnb_test_db (and only this database)
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test '@'localhost';

-- hbnb_test  should have SELECT privilege on the database performance_schema (and only this database)
GRANT SELECT ON performance_schema.* TO 'hbnb_test '@'localhost';

-- ascertain the changes apply
FLUSH PRIVILEGES;
