#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.db_storage import DBStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class TestDBStorage(unittest.TestCase):
    """Class to test dbstorage method"""
    @classmethod
    def setUpClass(cls):
        """set up class"""
        cls.engine = create_engine('sqlite:///test_db.sqlite')
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

        # Create the database schema
        Base.metadata.create_all(cls.engine)

    def setUp(self):
        """Initialize a fresh database session for each test"""
        self.db_storage = DBStorage()
        self.db_storage.reload()

    def test_add_state(self):
        """Get the number of current records in the states table"""
        initial_count = self.get_state_count()

        new_state = State(name="California")
        self.db_storage.new(new_state)
        self.db_storage.save()

        # Get the number of current records in the states table again
        final_count = self.get_state_count()

        # Assert that the difference is +1
        self.assertEqual(final_count - initial_count, 1)

    def get_state_count(self):
        """Query the database to count the number of State records"""
        return self.session.query(State).count()

    def test_add_city(self):
        """Get the number of current records in the cities table"""
        initial_count = self.get_city_count()

        new_city = City(name="San Jose")
        self.db_storage.new(new_city)
        self.db_storage.save()

        # Get the number of current records in the states table again
        final_count = self.get_city_count()

        # Assert that the difference is +1
        self.assertEqual(final_count - initial_count, 1)

    def get_city_count(self):
        """Query the database to count the number of State records"""
        return self.session.query(City).count()

    def test_add_amenity(self):
        """Get the number of current records in the cities table"""
        initial_count = self.get_amenity_count()

        new_amenity = Amenity(name="Wifi")
        self.db_storage.new(new_amenity)
        self.db_storage.save()

        # Get the number of current records in the states table again
        final_count = self.get_amenity_count()

        # Assert that the difference is +1
        self.assertEqual(final_count - initial_count, 1)

    def get_amenity_count(self):
        """Query the database to count the number of State records"""
        return self.session.query(Amenity).count()

    def test_add_place(self):
        """Get the number of current records in the cities table"""
        initial_count = self.get_place_count()

        new_place = Place(name="Wifi")
        self.db_storage.new(new_place)
        self.db_storage.save()

        # Get the number of current records in the states table again
        final_count = self.get_place_count()

        # Assert that the difference is +1
        self.assertEqual(final_count - initial_count, 1)

    def get_place_count(self):
        """Query the database to count the number of State records"""
        return self.session.query(Place).count()

    def test_add_review(self):
        """Get the number of current records in the cities table"""
        initial_count = self.get_review_count()

        new_review = Review(text="Never stay here")
        self.db_storage.new(new_review)
        self.db_storage.save()

        # Get the number of current records in the review table again
        final_count = self.get_review_count()

        # Assert that the difference is +1
        self.assertEqual(final_count - initial_count, 1)

    def get_review_count(self):
        """Query the database to count the number of State records"""
        return self.session.query(Review).count()

    def test_add_user(self):
        """Get the number of current records in the cities table"""
        initial_count = self.get_user_count()

        new_user = User(text="Never stay here")
        self.db_storage.new(new_user)
        self.db_storage.save()

        # Get the number of current records in the review table again
        final_count = self.get_user_count()

        # Assert that the difference is +1
        self.assertEqual(final_count - initial_count, 1)

    def get_user_count(self):
        """Query the database to count the number of State records"""
        return self.session.query(User).count()

    def test_add_basemodel(self):
        """Get the number of current records in the cities table"""
        initial_count = self.get_base_model_count()

        new_base_model = BaseModel(text="Never stay here")
        self.db_storage.new(new_base_model)
        self.db_storage.save()

        # Get the number of current records in the review table again
        final_count = self.get_base_model_count()

        # Assert that the difference is +1
        self.assertEqual(final_count - initial_count, 1)

    def get_base_model_count(self):
        """Query the database to count the number of State records"""
        return self.session.query(BaseModel).count()


if __name__ == "__main__":
    unittest.main()
