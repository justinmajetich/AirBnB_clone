-- MySQL server setup for development;
-- script creates database, db user and grants relevant privileges;

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- user auth: caching_sha2_password auth plugin
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
