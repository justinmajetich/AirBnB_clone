-- Prepare MySQL Server

-- Check if database hbnb_db exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Check if user hbnb_dev exists
SET @user_exists = (SELECT COUNT(*) FROM mysql.user WHERE user = 'hbnb_test');

-- If user does not exist, create it
IF @user_exists = 0 THEN
    CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
END IF;

-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;