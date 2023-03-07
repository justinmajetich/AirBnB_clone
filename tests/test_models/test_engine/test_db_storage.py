#!/usr/bin/python3
"""
Unit tests for DBStorage class
"""
import json
import models
import MySQLdb
import unittest
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine


class TestDBStorage(unittest.TestCase):
    """
    Test cases for DBStorage
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up test environment
        """
        if type(models.storage) == DBStorage:
            cls.storage = DBStorage()
            Base.metadata.create_all(cls.storage._DBStorage__engine)
            Session = sessionmaker(bind=cls.storage._DBStorage__engine)
            cls.storage._DBStorage__session = Session()
            cls.state = State(name="California")
            cls.storage._DBStorage__session.add(cls.state)
            cls.city = City(name="San_Jose", state_id=cls.state.id)
            cls.storage._DBStorage__session.add(cls.city)
            cls.user = User(email="poppy@holberton.com", password="betty")
            cls.storage._DBStorage__session.add(cls.user)
            cls.place = Place(city_id=cls.city.id, user_id=cls.user.id,
                              name="School")
            cls.storage._DBStorage__session.add(cls.place)
            cls.amenity = Amenity(name="Wifi")
            cls.storage._DBStorage__session.add(cls.amenity)
            cls.review = Review(place_id=cls.place.id, user_id=cls.user.id,
                                text="stellar")
            cls.storage._DBStorage__session.add(cls.review)
            cls.storage._DBStorage__session.commit()

    @classmethod
    def tearDownClass(cls):
        """
        Remove storage file at end of tests
        """
        if type(models.storage) == DBStorage:
            cls.storage._DBStorage__session.delete(cls.state)
            cls.storage._DBStorage__session.delete(cls.city)
            cls.storage._DBStorage__session.delete(cls.user)
            cls.storage._DBStorage__session.delete(cls.amenity)
            cls.storage._DBStorage__session.commit()
            cls.storage._DBStorage__session.close()

    @unittest.skipIf(type(models.storage) == models.engine.file_storage.FileStorage,
                     "Testing FileStorage")
    def test_all_cls(self):
        """
        Test DBStorage all method with a given class
        """
        obj = self.storage.all(State)
        self.assertEqual(type(obj), dict)
        self.assertEqual(len(obj), 1)
        self.assertEqual(self.state, list(obj.values())[0])

    def test_docstrings(self):
        """
        Test docstrings for DBStorage methods
        """
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)

    @unittest.skipIf(type(models.storage) == models.engine.file_storage.FileStorage,
                     "Testing FileStorage")
    def test_reload(self):
        """
        Test DBStorage reload method
        """
        og_session = self.storage._DBStorage__session
        self.storage.reload()
        self.assertIsInstance(self.storage._DBStorage__session, Session)
        self.assertNotEqual(og_session, self.storage._DBStorage__session)
        self.storage._DBStorage__session.close()
        self.storage._DBStorage__session = og_session

if __name__ == "__main__":
    unittest.main()