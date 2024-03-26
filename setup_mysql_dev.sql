-- creates new database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- creates new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@localhost IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@localhost;

-- grant SELECT privilege on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@localhost;
