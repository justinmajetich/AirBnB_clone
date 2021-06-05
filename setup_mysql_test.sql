-- creates a MySQL database and user with password and all privileges in new db,
-- plus SELECT privileges in performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
DROP USER IF EXISTS hbnb_test@localhost;
FLUSH PRIVILEGES;
CREATE USER hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL ON hbnb_test_db.* TO hbnb_test@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;