#!/usr/bin/python3
"""unittests for dbstorage"""

import models
from models.engine.db_storage import DBStorage
import unittest
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine
import uuid


class TestDBStorage(unittest.TestCase):
    """unittests for dbstorage"""

    @classmethod
    def setUpClass(cls):
        """create a new DBStorage Session"""
        cls.storage = DBStorage()
        Base.metadata.create_all(cls.storage._DBStorage__engine)
        Session = sessionmaker(bind=cls.storage._DBStorage__engine)
        cls.storage._DBStorage__session = Session()
        cls.state = State(name="Illinois")
        cls.storage._DBStorage__session.add(cls.state)
        cls.city = City(name="Chicago", state_id=cls.state.id)
        cls.storage._DBStorage__session.add(cls.city)
        cls.user = User(email="test@holberton.com", password="test")
        cls.storage._DBStorage__session.add(cls.user)
        cls.place = Place(city_id=cls.city.id, user_id=cls.user.id,
                          name="Hostel")
        cls.storage._DBStorage__session.add(cls.place)
        cls.amenity = Amenity(name="Wifi")
        cls.storage._DBStorage__session.add(cls.amenity)
        cls.review = Review(place_id=cls.place.id, user_id=cls.user.id,
                            text="Great")
        cls.storage._DBStorage__session.add(cls.review)
        cls.storage._DBStorage__session.commit()

    @classmethod
    def tearDownClass(cls):
        """
        Delete all instantiated test classes
        Close DBStorage session
        """
        if type(models.storage) == DBStorage:
            cls.storage._DBStorage__session.delete(cls.state)
            cls.storage._DBStorage__session.delete(cls.city)
            cls.storage._DBStorage__session.delete(cls.user)
            cls.storage._DBStorage__session.delete(cls.amenity)
            cls.storage._DBStorage__session.commit()
            del cls.User
            del cls.review
            del cls.place
            del cls.amenity
            del cls.state
            del cls.city

            cls.storage._DBStorage__session.close()

    def test_methods(self):
        """Check for methods."""
        self.assertTrue(hasattr(DBStorage, "__init__"))
        self.assertTrue(hasattr(DBStorage, "delete"))
        self.assertTrue(hasattr(DBStorage, "new"))
        self.assertTrue(hasattr(DBStorage, "all"))
        self.assertTrue(hasattr(DBStorage, "save"))
        self.assertTrue(hasattr(DBStorage, "reload"))

    def test_delete(self):
        """Test delete method"""
        s = State(name="Hawaii")
        self.storage._DBStorage__session.add(s)
        self.storage._DBStorage__session.commit()
        self.storage.delete(s)
        self.assertIn(s, list(self.storage._DBStorage__session.deleted))

    def test_all(self):
        """Test default all method."""
        obj = self.storage.all()
        self.assertEqual(type(obj), dict)
        self.assertEqual(len(obj), 6)

    def test_save(self):
        """Test save method"""
        s = State(name="Florida")
        self.storage._DBStorage__session.add(s)
        self.storage.save()
        obj = self.storage._DBStorage.__engine.query(State). \
            filter_by(name="FLorida")
        self.assertEqual(s.id, obj.id)

    def test_new(self):
        """Test new method"""
        s = State(name="Texas")
        self.storage.new(s)
        self.storage.flush()
        self.assertEqual(type(s.id), uuid.UUID)

    def test_reload(self):
        old_session = self.storage._DBStorage__session
        self.storage.reload()
        self.assertNotEqual(old_session, self.storage._DBStorage__session)


if __name__ == "__main__":
    unittest.main()
