#!/usr/bin/python3
"""
Defines unittests for the 'models/engine/db_storage.py' file.
"""
import models
import pep8
import MySQLdb
import unittest
import os
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine


class TestDatabaseDocs(unittest.TestCase):
    """Tests to check the documentation and style of Database classes"""
    @classmethod
    def setUpClass(cls):
        """DBStorage testing setup."""
        if type(models.storage) == DBStorage:
            cls.storage = DBStorage()
            Base.metadata.create_all(cls.storage._DBStorage__engine)
            Session = sessionmaker(bind=cls.storage._DBStorage__engine)
            cls.storage._DBStorage__session = Session()
            cls.state = State(name="Oklahoma")
            cls.storage._DBStorage__session.add(cls.state)
            cls.city = City(name="Tulsa", state_id=cls.state.id)
            cls.storage._DBStorage__session.add(cls.city)
            cls.user = User(email="betty@holberton.com", password="shnarf")
            cls.storage._DBStorage__session.add(cls.user)
            cls.place = Place(city_id=cls.city.id, user_id=cls.user.id,
                              name="Holberton")
            cls.storage._DBStorage__session.add(cls.place)
            cls.amenity = Amenity(name="Corn Holder")
            cls.storage._DBStorage__session.add(cls.amenity)
            cls.review = Review(place_id=cls.place.id, user_id=cls.user.id,
                                text="is gud")
            cls.storage._DBStorage__session.add(cls.review)
            cls.storage._DBStorage__session.commit()

    @classmethod
    def tearDownClass(cls):
        """DBStorage testing teardown."""
        if type(models.storage) == DBStorage:
            cls.storage._DBStorage__session.delete(cls.state)
            cls.storage._DBStorage__session.delete(cls.city)
            cls.storage._DBStorage__session.delete(cls.user)
            cls.storage._DBStorage__session.delete(cls.amenity)
            cls.storage._DBStorage__session.commit()
            del cls.state
            del cls.city
            del cls.user
            del cls.place
            del cls.amenity
            del cls.review
            cls.storage._DBStorage__session.close()
            del cls.storage

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_docstrings(self):
        """Test that all methods have docstrings."""
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_attributes(self):
        """Test that engine and session attributes exist."""
        self.assertTrue(isinstance(self.storage._DBStorage__engine, Engine))
        self.assertTrue(isinstance(self.storage._DBStorage__session, Session))

    def test_dbstorage_methods(self):
        self.assertTrue(hasattr(DBStorage, "__init__"))
        self.assertTrue(hasattr(DBStorage, "all"))
        self.assertTrue(hasattr(DBStorage, "new"))
        self.assertTrue(hasattr(DBStorage, "save"))
        self.assertTrue(hasattr(DBStorage, "delete"))
        self.assertTrue(hasattr(DBStorage, "reload"))

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_dbstorage_init(self):
        """Test initialization."""
        self.assertTrue(isinstance(self.storage, DBStorage))

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_dbstorage_all(self):
        """Test default all method."""
        obj = self.storage.all()
        self.assertEqual(type(obj), dict)
        self.assertEqual(len(obj), 6)

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_dbstorage_new(self):
        st = State(name="Oklahoma")
        self.storage.new(st)
        store = list(self.storage._DBStorage__session.new)
        self.assertIn(st, store)

    @unittest.skipIf(type(models.storage)
                     == FileStorage, "Testing FileStorage")
    def test_dbstorage_save(self):
        """Test save method."""
        st = State(name="Oklahoma")
        self.storage.new(st)
        self.storage.save()
        query = self.storage._DBStorage__session.query(State).all()
        self.assertIn(st, query)

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_dbstorage_delete(self):
        """Test delete method."""
        st = State(name="Oklahoma")
        self.storage.new(st)
        key = "{}.{}".format(type(st).__name__, st.id)
        self.storage.save()
        self.storage.delete(st)
        self.assertNotIn(key, self.storage.all().keys())

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE')
                     == 'db', "Testing DBStorage")
    def test_dbstorage_reload(self):
        """Test reload method."""
        # Create new state object and add to session
        st = State(name="Oklahoma")
        self.storage.new(st)
        self.storage.save()

        # Check if object is saved in the database
        query = self.storage._DBStorage__session.query(State).all()
        self.assertIn(st, query)

        # Clear session and recreate storage object
        self.storage._DBStorage__session.close()
        self.storage.reload()

        # Check that state object is still in the database
        query = self.storage._DBStorage__session.query(State).all()
        self.assertIn(st, query)


if __name__ == "__main__":
    unittest.main()