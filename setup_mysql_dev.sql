-- Prepares MySQL Server for AirBnB
-- Michael editted 1:41 PM
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS "hbnb_dev"@"localhost" IDENTIFIED BY "hbnb_dev_pwd";
GRANT SELECT ON performance_schema.* TO "hbnb_dev"@"localhost";
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO "hbnb_dev"@"localhost";
