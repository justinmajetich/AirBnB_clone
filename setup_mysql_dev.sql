-- script that prepares a MySQL server for the project if it does not already exist
-- database hbnb_dev_db
CREATE database IF NOT EXISTS hbnb_dev_db;

-- creates new user hbnb_dev (in localhost)
-- password of hbnb_dev should be set to hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
ALTER USER IF EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- ascertain the changes apply
FLUSH PRIVILEGES;
