-- Prepares a MySQL server for the hbnb project.
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

USE `hbnb_test_db`;

CREATE USER IF NOT EXISTS 'hbnb_test_db';

SET
    PASSWORD FOR 'hbnb_test' @'localhost' = 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test' @'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT
SELECT
    ON `performance_schema`.* TO 'hbnb_test' @'localhost' IDENTIFIED BY 'hbnb_test_pwd';
