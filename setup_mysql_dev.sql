-- create hbnb_dev_db database

CREATE database IF NOT EXISTS hbnb_dev_db;
-- create new user named 'hbnb_dev' with all privileges on the db
-- password hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- granting all privileges to this new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- select privilege for the user in the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
