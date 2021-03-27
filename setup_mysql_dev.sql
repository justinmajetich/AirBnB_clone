-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges on the db hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;
-- grant select privilege on the db performance_schema
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
