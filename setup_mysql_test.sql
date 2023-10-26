-- Prepares MySQL Server for AirBnB
-- Michael editted 1:50 PM
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS "hbnb_test"@"localhost" IDENTIFIED BY "hbnb_test_pwd";
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO "hbnb_test"@"localhost";
GRANT SELECT ON performance_schema.* TO "hbnb_test"@"localhost";