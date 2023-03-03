-- Creates database hbtn_test_db
CREATE DATABASE IF NOT EXISTS hbtn_test_db;
CREATE USER IF NOT EXISTS 'hbtn_test'@'localhost'
    IDENTIFIED BY 'hbtn_test_pwd';
GRANT ALL PRIVILEGES ON hbtn_test_db.* TO 'hbtn_test'@'localhost';
GRANT SELECT ON performance_schema.*
    TO 'hbtn_test'@'localhost';
FLUSH PRIVILEGES;