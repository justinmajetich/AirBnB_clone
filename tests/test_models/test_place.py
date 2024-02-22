#!/usr/bin/python3
"""
Unittest for the Class Place
"""
import os
import io
import unittest
import time
import datetime
import uuid
import pep8
import inspect
import models
import os
from unittest.mock import patch
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.user import User
from models.city import City
from models.state import State
from models.review import Review


class TestPlaceDocumentationAndStyle(unittest.TestCase):
    """
    Tests for the Place class documentation and style.
    """

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.place_funcs = inspect.getmembers(
                Place, predicate=inspect.isfunction
                )

    def test_pep8_conformance_Place(self):
        """
        Test that models/place.py conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/place.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_Place(self):
        """
        Test that tests/test_models/test_place.py
        conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["tests/test_models/test_place.py"]
        )
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_place_class_docstring(self):
        """
        Test for the Place class docstring
        """
        self.assertIsNot(
                Place.__doc__,
                None,
                "Place class needs a docstring"
                )
        self.assertTrue(
            len(Place.__doc__) >= 1, "Place class needs a docstring"
        )

    def test_place_func_docstrings(self):
        """
        Tests for the presence of docstrings in Place methods
        """
        for func in self.place_funcs:
            self.assertIsNot(
                func[1].__doc__,
                None,
                "{:s} method needs a docstring".format(func[0])
                )
            self.assertTrue(
                len(func[1].__doc__) >= 1,
                "{:s} method needs a docstring".format(func[0]),
                )


class Test_Place(unittest.TestCase):
    '''Test Place class'''
    def test_docstr(self):
        '''Test class documentaion'''
        self.assertTrue(len(Place.__doc__) > 2)

    def test_init(self):
        '''Test instances/cls attrs exists'''
        rev = Place()
        # instance(default) attrs
        self.assertTrue(hasattr(rev, 'id'))
        self.assertTrue(hasattr(rev, 'created_at'))
        self.assertTrue(hasattr(rev, 'updated_at'))
        # cls attrs
        self.assertTrue(hasattr(rev, 'city_id'))
        self.assertTrue(hasattr(rev, 'user_id'))
        self.assertTrue(hasattr(rev, 'name'))
        self.assertTrue(hasattr(rev, 'description'))
        self.assertTrue(hasattr(rev, 'number_rooms'))
        self.assertTrue(hasattr(rev, 'number_rooms'))
        self.assertTrue(hasattr(rev, 'number_bathrooms'))
        self.assertTrue(hasattr(rev, 'price_by_night'))
        self.assertTrue(hasattr(rev, 'latitude'))
        self.assertTrue(hasattr(rev, 'longitude'))
        self.assertTrue(hasattr(rev, 'amenity_ids'))

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db",
                     "To be tested in the FileStorage Mode only")
    def test_type_attrs(self):
        '''test instance types'''
        new = Place()
        self.assertEqual(type(new.city_id), str)
        self.assertEqual(type(new.user_id), str)
        self.assertEqual(type(new.name), str)
        self.assertEqual(type(new.description), str)
        self.assertEqual(type(new.number_rooms), int)
        self.assertEqual(type(new.number_bathrooms), int)
        self.assertEqual(type(new.max_guest), int)
        self.assertEqual(type(new.price_by_night), int)
        self.assertEqual(type(new.latitude), float)
        self.assertEqual(type(new.latitude), float)
        self.assertEqual(type(new.amenity_ids), list)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db",
                     "To be tested in the DBStorage Mode only")
    def test_attributes_db(self):
        """testing attributes in the db mode"""
        user = User(first_name="john", last_name="doe",
                    email="johndoe@gmail.com", password="123john")
        state = State(name="new york")
        city = City(name="new york", state_id=state.id)
        place = Place(city_id=city.id, user_id=user.id, name="lovely_place",
                      number_rooms=3, number_bathrooms=1, max_guest=6,
                      price_by_night=120, latitude=37.773972,
                      longitude=-122.431297)
        user.save()
        state.save()
        city.save()
        place.save()
        place_saved = models.storage._DBStorage__session.\
            query(Place).filter(Place.id == place.id).first()
        self.assertEqual(type(place_saved.user_id), str)
        self.assertEqual(type(place_saved.name), str)
        self.assertEqual(type(place_saved.number_rooms), int)
        self.assertEqual(type(place_saved.number_bathrooms), int)
        self.assertEqual(type(place_saved.max_guest), int)
        self.assertEqual(type(place_saved.price_by_night), int)
        self.assertEqual(type(place_saved.latitude), float)
        self.assertEqual(type(place_saved.latitude), float)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db",
                     "To be tested in the FileStorage Mode only")
    def test_place_reviews_file(self):
        """testing the review-place relationship"""
        user1 = User(first_name="John", last_name="Doe",
                     email="johndoe@gmail.com", password="123john")
        user2 = User(first_name="Mary", last_name="Jane",
                     email="maryj1@gmail.com", password="123mary")
        state = State(name="new york")
        city = City(name="new york", state_id=state.id)
        place = Place(city_id=city.id, user_id=user1.id, name="lovely_place",
                      number_rooms=3, number_bathrooms=1, max_guest=6,
                      price_by_night=120, latitude=37.773972,
                      longitude=-122.431297)
        review1 = Review(text="What a great hotel!",
                         place_id=place.id, user_id=user1.id)
        review2 = Review(text="LOVE IT!!!", place_id=place.id,
                         user_id=user2.id)
        user1.save()
        user2.save()
        state.save()
        city.save()
        place.save()
        review1.save()
        review2.save()
        self.assertTrue(isinstance(place.reviews, list))
        self.assertTrue(len(place.reviews) == 2)
        self.assertIn(review1, place.reviews)
        self.assertIn(review2, place.reviews)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db",
                     "To be tested in the FileStorage Mode only")
    def test_place_reviews_db(self):
        """testing the review-place relationship in db mode"""
        user1 = User(first_name="John", last_name="Doe",
                     email="johndoe@gmail.com", password="123john")
        user2 = User(first_name="Mary", last_name="Jane",
                     email="maryj1@gmail.com", password="123mary")
        state = State(name="new york")
        city = City(name="new york", state_id=state.id)
        place = Place(city_id=city.id, user_id=user1.id,
                      name="lovely_place", number_rooms=3,
                      number_bathrooms=1, max_guest=6,
                      price_by_night=120, latitude=37.773972,
                      longitude=-122.431297)
        review1 = Review(text="What a great hotel!",
                         place_id=place.id, user_id=user1.id)
        review2 = Review(text="LOVE IT!!!", place_id=place.id,
                         user_id=user2.id)
        user1.save()
        user2.save()
        state.save()
        city.save()
        place.save()
        review1.save()
        review2.save()
        self.assertTrue(len(place.reviews) == 2)
        self.assertIn(review1, place.reviews)
        self.assertIn(review2, place.reviews)
        list_reviews = models.storage._DBStorage__session.\
            query(Review).filter(Review.place_id == place.id).all()
        self.assertTrue(len(list_reviews) == 2)
        place.delete()
        list_reviews = models.storage._DBStorage__session.\
            query(Review).filter(Review.place_id == place.id).all()
        self.assertTrue(len(list_reviews) == 0)

    def test_args(self):
        '''Test anonymous arguments'''
        id = str(uuid.uuid4())
        rev = Place(id)
        self.assertNotEqual(id, rev.id)

    def test_kwargs(self):
        '''Test named arguments'''
        kw = {
                'id': 1, 'created_at': datetime.datetime.now(),
                'updated_at': datetime.datetime.now(),
             }
        # invalid date format
        with self.assertRaises(TypeError):
            Place(**kw)
        kw['created_at'] = datetime.datetime.now().isoformat()
        kw['updated_at'] = datetime.datetime.now().isoformat()
        rev = Place(**kw)
        self.assertEqual(rev.id, kw['id'])
        self.assertEqual(rev.created_at.isoformat(), kw['created_at'])
        self.assertEqual(rev.updated_at.isoformat(), kw['updated_at'])

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db",
                     "To be tested in the FileStorage Mode only")
    def test_save(self):
        '''Test saving object to file.json'''
        rev = Place()
        prev_date = rev.updated_at
        time.sleep(0.001)
        rev.save()
        curr_date = rev.updated_at
        self.assertIn('Place'+'.'+rev.id,
                      models.FileStorage._FileStorage__objects)
        self.assertNotEqual(prev_date.isoformat(), curr_date.isoformat())
        with self.assertRaises(TypeError):
            rev.save('')

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db",
                     "To be tested in the DBStorage Mode only")
    def test_save_db(self):
        """This function tests saving into a JSOM file"""
        user = User(first_name="John", last_name="Doe",
                    email="johndoe@gmail.com", password="123john")
        state = State(name="New York")
        city = City(name="New york", state_id=state.id)
        place = Place(city_id=city.id, user_id=user.id, name="Lovely_place",
                      number_rooms=3, number_bathrooms=1, max_guest=6,
                      price_by_night=120, latitude=37.773972,
                      longitude=-122.431297)
        user.save()
        state.save()
        city.save()
        place.save()
        place_saved = models.storage._DBStorage__session.\
            query(Place).filter(Place.id == place.id).first()
        self.assertEqual(place, place_saved)

    def test_to_dict(self):
        '''Test `to_dict` method'''
        rev = Place()
        dct = rev.to_dict()
        self.assertIn('__class__', dct)
        self.assertEqual('Place', dct['__class__'])
        with self.assertRaises(TypeError):
            rev.to_dict({'id': '123'})
            Place()

    def test_str(self):
        '''Test `Place` representaion'''
        with patch('sys.stdout', new_callable=io.StringIO) as m_stdout:
            rev = Place()
            print(rev)
            self.assertEqual(m_stdout.getvalue(),
                             '[Place] ({}) {}\n'.format(rev.id, rev.__dict__))


if __name__ == '__main__':
    unittest.main()
