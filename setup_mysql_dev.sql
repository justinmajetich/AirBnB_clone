-- Create the hbnb_dev_db database if it doesn't exist
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'hbnb_dev_db')
    CREATE DATABASE hbnb_dev_db;
-- Create the hbnb_dev user if it doesn't exist
 CREATE LOGIN hbnb_dev WITH PASSWORD = 'hbnb_dev_pwd';
-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON SCHEMA::dbo TO hbnb_dev;
-- Grant SELECT privilege on performance_schema to hbnb_dev
GRANT SELECT ON SCHEMA::performance_schema TO hbnb_dev;
