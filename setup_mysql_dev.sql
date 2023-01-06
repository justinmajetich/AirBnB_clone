-- Creating User and givig it permissions
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
GRANT USAGE ON *.*
      TO 'hbnb_dev'@'localhost'
      IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.*
      TO 'hbnb_dev'@'localhost'
      IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.*
      TO 'hbnb_dev'@'localhost'
      IDENTIFIED BY 'hbnb_dev_pwd';
FLUSH PRIVILEGES;
