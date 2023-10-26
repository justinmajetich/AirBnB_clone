-- Prepares MySQL test server for AirBNB
-- Michael editted 1:40 PM
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS "hbnb_test"@"localhost" IDENTIFIED BY "hbnb_test_pwd";
GRANT ALL PRIVILEGES ON perfomance_schema.* TO "hbnb_test"@"localhost";
GRANT SELECT ON hbnb_test_db.* TO "hbnb_test"@"localhost";
