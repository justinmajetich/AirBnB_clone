#!/usr/bin/python3
"""
   Test module for db_storage.py
"""
from models.engine.db_storage import DBStorage
from os import getenv
import unittest

storage = getenv('HBNB_TYPE_STORAGE')
@unittest.skipIf(storage != 'db', 'test case not for DBStorage')


class DBStorageTestCase(unittest.TestCase):
    """test for DBStorage"""

    def test_documentation(self):
        """test for object documentation"""
        self.assertIsNot(DBStorage.__doc__, None)

    def test_init(self):
        db_storage = DBStorage(storage)

        self.assertEqual(db_storage.__engine.url.username, "hbnb_dev")
        self.assertEqual(db_storage.__engine.url.password, "hbnb_dev_pwd")
        self.assertEqual(db_storage.__engine.url.host, "localhost")
        self.assertEqual(db_storage.__engine.url.database, "hbnb_test_db")

        self.assertTrue(db_storage.__engine.pool.pre_ping)

    def test_all(self):
        db_storage = DBStorage()

        user = User(name="John Doe", email="john.doe@example.com", password="password")
        state = State(name="California")
        city = City(name="San Francisco", state=state)
        place = Place(name="Golden Gate Bridge", city=city)
        amenity = Amenity(name="WiFi")
        review = Review(place=place, user=user, text="This place is amazing!")

        db_storage.new(user)
        db_storage.new(state)
        db_storage.new(city)
        db_storage.new(place)
        db_storage.new(amenity)
        db_storage.new(review)

        db_storage.commit()

        objects = db_storage.all()

        self.assertEqual(len(objects), 6)

        self.assertIn(f"{User.__name__}.{user.id}", objects)
        self.assertIn(f"{State.__name__}.{state.id}", objects)
        self.assertIn(f"{City.__name__}.{city.id}", objects)
        self.assertIn(f"{Place.__name__}.{place.id}", objects)
        self.assertIn(f"{Amenity.__name__}.{amenity.id}", objects)
        self.assertIn(f"{Review.__name__}.{review.id}", objects)

    def test_new(self):
        db_storage = DBStorage()

        user = User(name="John Doe", email="john.doe@example.com", password="password")

        db_storage.new(user)

        db_storage.commit()

        objects = db_storage.all(User)
        self.assertEqual(len(objects), 1)
        self.assertIn(f"{User.__name__}.{user.id}", objects)

        try:
            db_storage.new(user)
        except Exception as e:
            self.assertEqual(str(e), "Object already exists in the database")
        else:
            self.fail("Expected an exception to be raised")
