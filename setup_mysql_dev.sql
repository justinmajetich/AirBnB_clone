-- Creation of db if not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creation of the hbnb_dev user
CREATE USER IF NOT EXISTS "hbnb_dev"@"localhost" IDENTIFIED BY "hbnb_dev_pwd";

-- Granting all privilages to user hbnb_dev to hbnb_dev_db database
GRANT ALL PRIVILEGES ON hbnb_dev_db. * TO "hbnb_dev"@"localhost";
GRANT SELECT ON performance_schema.* To "hbnb_dev"@"localhost";

FLUSH PRIVILEGES;
