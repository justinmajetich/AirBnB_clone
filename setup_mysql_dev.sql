-- Create the hbnb_dev_db database if it doesn't exist
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'hbnb_dev_db')
    CREATE DATABASE hbnb_dev_db;
-- Create the hbnb_dev user if it doesn't exist
 CREATE LOGIN hbnb_dev WITH PASSWORD = 'hbnb_dev_pwd';
-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON SCHEMA::dbo TO hbnb_dev;
-- Grant SELECT privilege on performance_schema to hbnb_dev
GRANT SELECT ON SCHEMA::performance_schema TO hbnb_dev;

-- Create the hbnb_test_db database if it doesn't exist
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'hbnb_test_db')
    CREATE DATABASE hbnb_test_db;

-- Create the hbnb_test user if it doesn't exist
IF NOT EXISTS (SELECT * FROM sys.syslogins WHERE name = 'hbnb_test')
    CREATE LOGIN hbnb_test WITH PASSWORD = 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to hbnb_test
USE hbnb_test_db;
IF NOT EXISTS (SELECT * FROM sys.database_principals WHERE name = 'hbnb_test')
    CREATE USER hbnb_test FOR LOGIN hbnb_test;
ALTER ROLE db_owner ADD MEMBER hbnb_test;

-- Grant SELECT privilege on performance_schema to hbnb_test
GRANT SELECT ON SCHEMA::performance_schema TO hbnb_test;
