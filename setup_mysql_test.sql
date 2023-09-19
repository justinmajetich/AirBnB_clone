-- THIS SCRIPT SETS UP THE MYSQL SERVER FOR THE HBNB V2 project
-- CREATING hbnb_dev db User
CREATE USER IF NOT EXISTS "hbnb_test"@"localhost" IDENTIFIED BY "hbnb_test_pwd";

-- CREATING database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- GRANTING hbnb_dev all permissions to hbnb_dev_db
GRANT ALL ON hbnb_test_db.* TO "hbnb_test"@"localhost";
GRANT SELECT ON performance_schema.* TO "hbnb_test"@"localhost";
