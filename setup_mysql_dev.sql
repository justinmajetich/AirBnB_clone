--
-- Creating Database
--

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

--
-- Creating User
--

CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';

--
-- Granting Privileges
--

GRANT ALL ON hbnb_dev_db.* TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;

