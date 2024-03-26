-- Création de la base de données hbnb_dev_db si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Création de l'utilisateur hbnb_dev s'il n'existe pas déjà, avec le mot de passe hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Attribution de tous les privilèges à l'utilisateur hbnb_dev sur la base de données hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Attribution du privilège SELECT à l'utilisateur hbnb_dev sur la base de données performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
