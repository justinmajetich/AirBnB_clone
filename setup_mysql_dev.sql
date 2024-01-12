-- Prepara un servidor MySQL para el proyecto:
-- Crea una BD hbnb_dev_db.
-- Crea un usuario hbnb_dev y contraseña hbnb_dev_pwd en el localhost
-- Otorga privilegios a USER y a la database
-- Otorgar el privilegio SELECT a la performance_schema

-- Crea una BD si no existe
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Crea un usuario si no existe
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Otorga todos los privilegios a hbnb_dev_db hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';

-- Otorga el privilegios SELECT a performance_schema de hbnb_dev
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';

-- Vaciar privilegios para aplicar cambio
FLUSH PRIVILEGES;
