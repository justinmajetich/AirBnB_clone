-- Prepares a MySQL server

-- Database creation
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- creation of user
CREATE USER IF NOT EXISTS "hbnb_test"@"localhost" IDENTIFIED BY "hbnb_test_pwd";

-- grant all privilages on hbnb_test_db database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO "hbnb_test"@"localhost";

-- grant select privilage on performace_schema
GRANT SELECT ON performance_schema.* TO "hbnb_test"@"localhost";

FLUSH PRIVILEGES;
