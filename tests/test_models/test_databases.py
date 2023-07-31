import unittest
import MySQLdb

# Clase que define las pruebas unitarias
class TestCreateState(unittest.TestCase):

    def setUp(self):
        # Establecer la conexión con la base de datos
        self.conn = MySQLdb.connect(user='tu_usuario', passwd='tu_contraseña', db='tu_base_de_datos', host='tu_host')
        self.cursor = self.conn.cursor()

        # Asegurarse de que la tabla "states" esté vacía antes de cada prueba
        self.cursor.execute("DELETE FROM states;")
        self.conn.commit()

    def tearDown(self):
        # Cerrar la conexión y limpiar después de cada prueba
        self.cursor.close()
        self.conn.close()

    def test_create_state(self):
        # Obtener el número de registros antes de ejecutar el comando
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        initial_records = self.cursor.fetchone()[0]

        # Aquí simulas la ejecución del comando en la consola
        # Supongamos que ejecutas el comando create State name="California" en la consola
        # Por ejemplo, podrías hacer algo como:
        # self.cursor.execute("INSERT INTO states (name) VALUES ('California');")
        # self.conn.commit()

        # Obtener el número de registros después de ejecutar el comando
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        final_records = self.cursor.fetchone()[0]

        # Validar que la diferencia sea +1
        self.assertEqual(final_records - initial_records, 1)

if __name__ == '__main__':
    unittest.main()
