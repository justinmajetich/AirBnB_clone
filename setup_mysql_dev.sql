-- create a database called hbnb_dev_db
-- create a new user hbnb_dev
-- set user password
-- set user to have all priveleges only in this database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_de' @ 'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev' @ 'localhost';
FLUSH PRIVELEGES;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVELEGES;
