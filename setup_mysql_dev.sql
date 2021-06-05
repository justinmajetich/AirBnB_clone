-- creates a MySQL database and user with password and all privileges in new db,
-- plus SELECT privileges in performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
DROP USER IF EXISTS hbnb_dev@localhost;
FLUSH PRIVILEGES;
CREATE USER hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db.* TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
