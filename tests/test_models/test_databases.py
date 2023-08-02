import unittest
import MySQLdb

# Función para conectar con la base de datos MySQL y obtener el número de registros en la tabla states
def get_number_of_records():
    conn = MySQLdb.connect(user='hbnb_test', passwd='hbnb_test_pwd', db='hbnb_test_db', host='localhost')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM states;")
    result = cursor.fetchone()
    conn.close()
    return result[0]

# Clase que define las pruebas de integración con MySQL
class TestMySQLIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Establecer la conexión con la base de datos antes de ejecutar todas las pruebas
        cls.conn = MySQLdb.connect(user='hbnb_test', passwd='hbnb_test_pwd', db='hbnb_test_db', host='localhost')
        cls.cursor = cls.conn.cursor()

        # Asegurarse de que la tabla "states" esté vacía antes de ejecutar todas las pruebas
        cls.cursor.execute("DELETE FROM states;")
        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        # Cerrar la conexión y limpiar después de ejecutar todas las pruebas
        cls.cursor.close()
        cls.conn.close()

    def test_create_state(self):
        # Obtener el número de registros antes de ejecutar el comando
        initial_records = get_number_of_records()
        
        # Aquí simulas la ejecución del comando en la consola
        # Supongamos que ejecutas el comando create State name="California" en la consola
        # Por ejemplo, podrías hacer algo como:
        # self.cursor.execute("INSERT INTO states (name) VALUES ('California');")
        # self.conn.commit()

        # Obtener el número de registros después de ejecutar el comando
        final_records = get_number_of_records()

        # Validar que la diferencia sea +1
        self.assertEqual(final_records - initial_records, 1)

if __name__ == '__main__':
    unittest.main()
