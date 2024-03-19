-- Set up Mysql Server
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev' @'localhost' IDENTIFIED
WITH
    caching_sha2_password BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev' @'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_dev' @'localhost';