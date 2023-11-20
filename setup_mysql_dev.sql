--creates a hbnb_dev_db database if non exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
--create user hbnb_dev if non exist identifiy by password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--Grant all priviledges to hbnb_dev on hbnb_dev_db database
GRANT ALL PRIVILEDGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
--grant SELECT priviledge on db perfomance shema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'


--FLUSH PRIVILEDGES
