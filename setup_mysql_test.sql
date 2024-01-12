-- Prepares a MySQL Test server for the project.
-- Crea una BD hbnb_test_db.
-- Crea un usuario hbnb_test y contraseña hbnb_test_pwd en el localhost
-- Otorga privilegios a USER y a la database
-- Otorgar el privilegio SELECT a la performance_schema

-- Crea una BD si no existe
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Crea un usuario si no existe
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Otorga todos los privilegios a hbnb_test_db hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO 'hbnb_test'@'localhost';

-- Otorga el privilegios SELECT a performance_schema de hbnb_test
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';

-- Vaciar privilegios para aplicar cambio
FLUSH PRIVILEGES;

