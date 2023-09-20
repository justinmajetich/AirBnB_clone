-- Creating the hbnb_test_db database and the user hbnb_test
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;
CREATE USER IF NOT EXISTS "hbnb_test"@"localhost" IDENTIFIED BY "hbnb_test_pwd";
GRANT ALL PREVELEGES ON `hbnb_test_db`.* TO "hbnb_test"@"localhost";
GRANT SELECT ON `performance_schema`.* TO "hbnb_test"@"localhost";
FLUSH PRIVILEGES;
