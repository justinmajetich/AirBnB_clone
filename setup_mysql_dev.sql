-- THIS SCRIPT SETS UP THE MYSQL SERVER FOR THE HBNB V2 project
-- CREATING hbnb_dev db User
CREATE USER IF NOT EXISTS "hbnb_dev"@"localhost" IDENTIFIED BY "hbnb_dev_pwd";

-- CREATING database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- GRANTING hbnb_dev all permissions to hbnb_dev_db
GRANT ALL ON hbnb_dev_db.* TO "hbnb_dev"@"localhost";
GRANT SELECT ON performance_schema.* TO "hbnb_dev"@"localhost";
