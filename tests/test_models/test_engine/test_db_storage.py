import unittest
import os
import tempfile
from models import storage
from models.engine.db_storage import DBStorage
from models.state import State


class TestDBStorage(unittest.TestCase):
    """Test Case """

    @classmethod
    def setUpClass(cls):
        """ """
        cls.db_fd, cls.db_path = tempfile.mkstemp()
        os.environ['HBNB_TYPE_STORAGE'] = 'db'
        storage._FileStorage__objects.clear()
        cls.storage = DBStorage()
        cls.storage.reload()

    @classmethod
    def tearDownClass(cls):
        """
        configures a database to be used as a data storage medium
        """
        os.close(cls.db_fd)
        os.unlink(cls.db_path)

    def setUp(self):
        """
        initializes the database of the data storage
        instance for the test by removing all objects of the State class
        """
        self.session = self.storage._DBStorage__session
        self.session.query(State).delete()
        self.session.commit()

    def tearDown(self):
        """
        performs cleaning operations
        """
        self.session.query(State).delete()
        self.session.commit()

    def test_objects(self):
        """
        checks the object type
        """
        self.assertEqual(type(self.storage.all()), dict)

    def test_storage(self):
        """
        verifica si un objeto creado a través de la clase State
        """
        new = State(name="Florida")
        new.save()
        _id = new.to_dict()['id']
        self.assertIn(new.__class__.__name__ + '.' + _id,
                        self.storage.all(type(new)).keys())

    def test_storage_created(self):
        """
        verifica si la instancia de almacenamiento de dato
        en el sistema se crea correctamente como una
        instancia de la clase DBStorage.
        """
        self.assertEqual(type(self.storage), DBStorage)
    
    def test_empty_database(self):
        """
        verifica si la instancia de almacenamiento
        de datos en el sistema está vacía.
        """
        self.assertEqual(len(self.storage.all()), 0)
