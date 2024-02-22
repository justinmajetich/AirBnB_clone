-- Prepare MySQL Server

-- Check if database hbnb_db exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Check if user hbnb_dev exists
SET @user_exists = (SELECT COUNT(*) FROM mysql.user WHERE user = 'hbnb_dev');

-- If user does not exist, create it
IF @user_exists = 0 THEN
    CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
END IF;

-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;