<<<<<<< HEAD
-- CREATES DATABASE AND A USER WITH PERMISSIONS
=======
-- CREATES DATABASE AND USER WITH PERMISSIONS
>>>>>>> a293e5c3798ce6357468ef5d9b40c5e09b3c9fe5
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
