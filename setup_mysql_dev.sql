--A script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE DATABASE IF NOT EXISTS performance_schema;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;