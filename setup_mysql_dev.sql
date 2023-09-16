-- Sets up a Sql database and user
-- crate databse hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create user
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';

-- choose databse
USE hbnb_dev_db

-- grant permisions to hbnb_dev on hbnb_dev_db
GRANT ALL ON hbnb_dev_db.* TO hbnb_dev@localhost;

-- grant permisions to hbnb_dev on performance_schema
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
