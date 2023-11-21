--creates a a database hbnb_dev_db
--creates new user hbnb_dev in localhost
--sets password for hbnb_dev to (hbnb_dev_pwd)
--sets all privilages on the hbnb_dev_db for hbnb_dev (only in this db)
--sets SELECT privilages on the db performance_schema
--if db hbnb_dev_db || hbnb_dev exits, script should not fail

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES on hbnb_dev_db.* to 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

