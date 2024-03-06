#!/usr/bin/python3

import inspect
import unittest
import MySQLdb
import pycodestyle as pep8
import os
from sqlalchemy.orm import Session
from models.engine import db_storage
from models.engine.db_storage import DBStorage
from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


def createCursor():
    """
    This function creates a cursor for the MySQLdb
    """
    cur = MySQLdb.connect(host=os.getenv("HBNB_MYSQL_HOST"),
                          port=3306,
                          user=os.getenv("HBNB_MYSQL_USER"),
                          passwd=os.getenv("HBNB_MYSQL_PWD"),
                          db=os.getenv("HBNB_MYSQL_DB")
                          )
    return cur.cursor()


class TestDBStorageDocumentationAndStyle(unittest.TestCase):
    """
    Tests for the DBStorage class documentation and style.
    """

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.db_funcs = inspect.getmembers(
                DBStorage, predicate=inspect.isfunction
                )

    def test_pep8_conformance_db_storage(self):
        """
        Test that models/engine/db_storage.py conforms to PEP8.
        """
        pep8style = pep8.StyleGuide()
        result = pep8style.check_files(["models/engine/db_storage.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_db_storage(self):
        """
        Test that tests/test_models/test_engine/test_db_storage.py
        conforms to PEP8.
        """
        pep8style = pep8.StyleGuide()
        result = pep8style.check_files(
            ["tests/test_models/test_engine/test_db_storage.py"]
        )
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_db_storage_module_docstring(self):
        """
        Test for the db_storage module docstring
        """
        self.assertIsNot(
                db_storage.__doc__,
                None,
                "db_storage.py needs a docstring"
                )
        self.assertTrue(
                len(db_storage.__doc__) >= 1,
                "db_storage.py needs a docstring"
                )

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(
                DBStorage.__doc__,
                None,
                "DBStorage class needs a docstring"
                )
        self.assertTrue(
            len(DBStorage.__doc__) >= 1, "DBStorage class needs a docstring"
        )

    def test_db_func_docstrings(self):
        """
        Tests for the presence of docstrings in DBStorage methods
        """
        for func in self.db_funcs:
            self.assertIsNot(
                func[1].__doc__,
                None,
                "{:s} method needs a docstring".format(func[0])
                )
            self.assertTrue(
                len(func[1].__doc__) >= 1,
                "{:s} method needs a docstring".format(func[0]),
            )


@unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db',
        "skip if not database storage"
        )
class TestDBStorage(unittest.TestCase):
    """Test for the DBStorage class"""
    def setUp(self):
        """Set up for the tests"""
        self.__session = Session()
        self.storage = storage
        self.instances = {}

        # Create and save State instance
        self.instances['State'] = State(name="California")
        self.storage.new(self.instances['State'])
        self.storage.save()

        # Create and save User instance
        self.instances['User'] = User(
                email="user@mail.com",
                password="123",
                )
        self.storage.new(self.instances['User'])
        self.storage.save()

        # create City instance
        self.instances['City'] = City(
                name="San_Francisco",
                state_id=self.instances['State'].id
                )
        self.storage.new(self.instances['City'])
        self.storage.save()

        # create Place instance
        self.instances['Place'] = Place(
                name="House",
                city_id=self.instances['City'].id,
                user_id=self.instances['User'].id
                )
        self.storage.new(self.instances['Place'])
        self.storage.save()

        # create Review instance
        self.instances['Review'] = Review(
                text="Great_place",
                place_id=self.instances['Place'].id,
                user_id=self.instances['User'].id
                )
        self.storage.new(self.instances['Review'])
        self.storage.save()

        # Create and save Amenity instance
        self.instances['Amenity'] = Amenity(name="Wifi")
        self.storage.new(self.instances['Amenity'])
        self.storage.save()

        # append Amenity to Place
        #  self.instances['Place'].amenities.append(self.instances['Amenity'])
        #  self.storage.save()
        #  self.storage.reload()

        self.cursor = createCursor()

    def tearDown(self):
        """Tear down the tests"""
        ignore = ['City', 'Review', 'Place']
        for k, instance in self.instances.items():
            if k not in ignore:
                instance.delete()

        self.storage.save()
        self.cursor.close()

    def test_all(self):
        """Test the all method"""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.cursor.close()
        self.cursor = createCursor()
        classes = ['users', 'states', 'cities', 'places',
                   'reviews', 'amenities']
        rows = []
        for cl in classes:
            self.cursor.execute("SELECT * FROM {}".format(cl))
            rows.extend(self.cursor.fetchall())

        self.assertEqual(len(all_objs), len(rows))

    def test_new(self):
        """Test the new method"""
        new_state = State(name="Nevada")
        new_state.save()
        self.cursor.close()
        self.cursor = createCursor()
        self.cursor.execute("SELECT * FROM states WHERE id='{}'"
                            .format(new_state.id))
        row = self.cursor.fetchone()
        self.assertIn(new_state.name, row)
        self.assertIn(new_state, self.storage.all(State).values())

    def test_save(self):
        """Test the save method"""
        new_state = State(name="Nevada")
        self.storage.new(new_state)
        self.storage.save()
        self.assertIn(new_state, self.storage.all(State).values())

    def test_delete(self):
        """Test the delete method"""
        new_state = State(name="Nevada")
        self.storage.new(new_state)
        self.storage.save()
        self.storage.delete(new_state)
        self.assertNotIn(new_state, self.storage.all(State).values())


if __name__ == "__main__":
    unittest.main()
