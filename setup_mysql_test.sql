--Prepare a MySQL database for testing
CREATE DATABASE IF NOT EXISTS hbnb_dev_test_db;

CREATE user IF NOT EXISTS 'hbnb_dev_test' @'localhost' IDENTIFIED BY 'hbnb_dev_tets_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_test_db.* TO 'hbnb_dev_test' @'localhost';

GRANT
SELECT
    ON performance_schema.* TO 'hbnb_dev_test' @'localhost';