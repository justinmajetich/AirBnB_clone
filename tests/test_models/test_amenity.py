#!/usr/bin/python3
"""
Unittest for the Class "Amenity"
"""

import os
import inspect
import pep8
import unittest
import datetime
import models
import os
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.state import State
from models.place import Place


class TestAmenityDocumentationAndStyle(unittest.TestCase):
    """
    Tests for the DBStorage class documentation and style.
    """

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.amenity_funcs = inspect.getmembers(
                Amenity, predicate=inspect.isfunction
                )

    def test_pep8_conformance_Amenity(self):
        """
        Test that models/amenity conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/amenity.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_Amenity(self):
        """
        Test that tests/test_models/test_amenity.py
        conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["tests/test_models/test_amenity.py"]
        )
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_amenity_class_docstring(self):
        """
        Test for the Amenity class docstring
        """
        self.assertIsNot(
                Amenity.__doc__,
                None,
                "Amenity class needs a docstring"
                )
        self.assertTrue(
            len(Amenity.__doc__) >= 1, "Amenity class needs a docstring"
        )

    def test_amenity_func_docstrings(self):
        """
        Tests for the presence of docstrings in Amenity methods
        """
        for func in self.amenity_funcs:
            self.assertIsNot(
                func[1].__doc__,
                None,
                "{:s} method needs a docstring".format(func[0])
                )
            self.assertTrue(
                len(func[1].__doc__) >= 1,
                "{:s} method needs a docstring".format(func[0]),
                )


class Test_Amenity(unittest.TestCase):
    """This class defines unittests for the different attributes both inherited
    and unique for the Amenity Class"""

    def test_uniq_time(self):
        """This function tests for the uniquenss of time creation"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.created_at, amenity2.created_at)

    def test_uniq_id(self):
        """This function tests for the uniqueness of the id"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_custom_id(self):
        """This function creates a Amenity with a specific ID"""
        amenity = Amenity()
        amenity.id = "123456"
        self.assertEqual(amenity.id, "123456")

    def test_type_id(self):
        """This function tests the type of id attr"""
        self.assertIs(type(Amenity().id), str)

    def test_type_created_at(self):
        """This function tests the type of created_at attr"""
        self.assertIs(type(Amenity().created_at), datetime.datetime)

    def test_type_updated_at(self):
        """This function tests for the type of updated_at attr"""
        self.assertIs(type(Amenity().updated_at), datetime.datetime)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db",
                     "To be tested in the FileStorage Mode only")
    def test_type_name(self):
        """This function tests the type of name attr"""
        self.assertIs(type(Amenity().name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db",
                     "To be tested in the DBStorage Mode only")
    def test_attributes_db(self):
        """Testing the attributes in the db mode"""
        amenity = Amenity(name="TV")
        amenity.save()
        amenity_saved = models.storage._DBStorage__session.\
            query(Amenity).filter(Amenity.id == amenity.id).first()
        self.assertIs(type(amenity_saved.id), str)
        self.assertIs(type(amenity_saved.created_at), datetime.datetime)
        self.assertIs(type(amenity_saved.updated_at), datetime.datetime)
        self.assertEqual(type(amenity_saved.name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db",
                     "To be tested in the DBStorage Mode only")
    def test_save_db(self):
        """This function tests saving into a JSOM file"""
        amenity = Amenity(name="TV")
        amenity.save()
        saved_am = models.storage._DBStorage__session.\
            query(Amenity).filter(Amenity.id == amenity.id).first()
        self.assertEqual(amenity, saved_am)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db",
                     "To be tested in the FileStorage Mode only")
    def test_obj_storage(self):
        """This function tests that an object is automatically saved in
        the ___objects attr of storage instance"""
        amenity = Amenity()
        amenity.save()
        self.assertIn(amenity, models.storage.all().values())

    def test_type_class(self):
        """This function tests the type of an instance created"""
        self.assertIs(type(Amenity()), Amenity)

    def test_str(self):
        """This funtion tests string representation of a BaseModel"""
        amenity = Amenity()
        amenity.id = "123456"
        tdy = datetime.datetime.today()
        amenity.created_at = amenity.updated_at = tdy
        self.assertIn("[Amenity] (123456)", amenity.__str__())
        self.assertIn("'id': '123456'", amenity.__str__())
        self.assertIn("'created_at': " + repr(tdy), amenity.__str__())
        self.assertIn("'updated_at': " + repr(tdy), amenity.__str__())

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db",
                     "To be tested in the FileStorage Mode only")
    def test_place_reviews_db(self):
        """testing the amenity-place relationship"""
        user = User(first_name="John", last_name="Doe",
                    email="johndoe@gmail.com", password="123john")
        state = State(name="new york")
        city = City(name="new york", state_id=state.id)
        place1 = Place(city_id=city.id, user_id=user.id,
                       name="lovely_place", number_rooms=3,
                       number_bathrooms=1, max_guest=6,
                       price_by_night=120, latitude=37.773972,
                       longitude=-122.431297)
        place2 = Place(city_id=city.id, user_id=user.id,
                       name="green_room", number_rooms=1,
                       number_bathrooms=1, max_guest=2,
                       price_by_night=300, latitude=35.43272,
                       longitude=-192.54597)
        amenity1 = Amenity(name="TV")
        amenity2 = Amenity(name="Pets_allowed")
        user.save()
        state.save()
        city.save()
        place1.save()
        place2.save()
        amenity1.save()
        amenity2.save()

        place1.amenities.append(amenity1)
        place1.amenities.append(amenity2)
        place2.amenities.append(amenity1)
        place2.amenities.append(amenity2)
        place1.save()
        place2.save()
        amenity1.save()
        amenity2.save()
        self.assertTrue(len(amenity1.place_amenity) == 2)
        self.assertTrue(isinstance(amenity1.place_amenity, list))
        self.assertIn(place1, amenity1.place_amenity)
        self.assertIn(place2, amenity1.place_amenity)


class Test_instantation(unittest.TestCase):
    """This class tests the instantation of a Amenity class"""

    def test_init_kwargs(self):
        """This function create a Amenity with kwargs"""
        tdy = datetime.datetime.today()
        amenity = Amenity(id="123456", created_at=tdy.isoformat(),
                          updated_at=tdy.isoformat(), name="spa")
        self.assertEqual(amenity.id, "123456")
        self.assertEqual(amenity.created_at, tdy)
        self.assertEqual(amenity.updated_at, tdy)
        self.assertEqual(amenity.name, "spa")

    def test_init_args(self):
        """This function creates a Amenity without args"""
        tdy = datetime.datetime.today()
        amenity = Amenity("7890", id="4567", created_at=tdy.isoformat(),
                          updated_at=tdy.isoformat())
        self.assertEqual(amenity.id, "4567")
        self.assertEqual(amenity.created_at, tdy)
        self.assertEqual(amenity.updated_at, tdy)

    def teat_init_class(self):
        """This function tests giving args a class key"""
        amenity1 = Amenity()
        dict_amenity1 = amenity1.to_dict()
        dict_amenity1['__class__'] = "BaseModel"
        amenity2 = Amenity(**dict_amenity1)
        dict_amenity2 = amenity2.to_dict()
        self.assertEqual(dict_amenity2['__class__'], "Amenity")


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db",
                 "To be tested in the FileStorage Mode only")
class Test_save(unittest.TestCase):
    """This class tests the instance method save(self)"""

    def test_save(self):
        """This function tests updating the time"""
        amenity = Amenity()
        old_time = amenity.updated_at
        amenity.save()
        self.assertNotEqual(amenity.updated_at, old_time)

    def test_two_save(self):
        """This function tests updates the time twice"""
        amenity = Amenity()
        first_time = amenity.updated_at
        amenity.save()
        self.assertNotEqual(amenity.updated_at, first_time)
        second_time = amenity.updated_at
        amenity.save()
        self.assertNotEqual(amenity.updated_at, second_time)

    def test_save_args(self):
        """This function give save method an argument"""
        with self.assertRaises(TypeError):
            Amenity().save("arg")

    def test_save_file(self):
        """This function tests saving into a JSOM file"""
        amenity = Amenity()
        amenity.save()
        with open(models.storage._FileStorage__file_path,
                  encoding="utf-8") as f:
            self.assertIn("Amenity." + amenity.id, f.read())


class Test_to_dict(unittest.TestCase):
    """unittests for the instance method to_dict"""

    def test_type_dict(self):
        """This function tests the type of to_dict return value"""
        self.assertIs(type(Amenity().to_dict()), dict)

    def test_contents_dict(self):
        """This function tests the contents of a dictionary"""
        amenity = Amenity()
        self.assertIn('updated_at', amenity.to_dict())
        self.assertIn('__class__', amenity.to_dict())
        self.assertIn('id', amenity.to_dict())
        self.assertIn('created_at', amenity.to_dict())

    def test_dynamic_dict(self):
        """This function tests the dynamic creation of attributes in dict"""
        amenity = Amenity()
        amenity.country = "US"
        amenity.postal_code = 456
        self.assertIn('country', amenity.to_dict())
        self.assertIn('postal_code', amenity.to_dict())

    def test_type_time_in_dict(self):
        """This function tests the type of created_at and updated_at in dict"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIs(type(amenity_dict['created_at']), str)
        self.assertIs(type(amenity_dict['updated_at']), str)

    def test_dict_kwargs(self):
        """This function create a User with kwargs and tests its dict"""
        tdy = datetime.datetime.today()
        amenity = Amenity(id="123456", created_at=tdy.isoformat(),
                          updated_at=tdy.isoformat(), name="spa")
        amenity_dict = amenity.to_dict()
        self.assertIn('name', amenity_dict)

    def test_full_dict(self):
        """This function tests creation of a dictionary"""
        amenity = Amenity()
        amenity.id = "123456"
        tdy = datetime.datetime.today()
        amenity.created_at = amenity.updated_at = tdy
        dict_amenity = {'__class__': 'Amenity',
                        'updated_at': tdy.isoformat(),
                        'created_at': tdy.isoformat(),
                        'id': "123456"}
        self.assertDictEqual(amenity.to_dict(), dict_amenity)

    def test_dict_class(self):
        """This function tests that __dict__ repr and to_dict()
        are different"""
        amenity = Amenity()
        self.assertNotEqual(amenity.__dict__, amenity.to_dict())

    def test_to_dict_arg(self):
        """This function tests giving the instance method to_dict arguments"""
        with self.assertRaises(TypeError):
            Amenity().to_dict("arg")

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db",
                     "To be tested in the FileStorage Mode only")
    def test_delete_db(self):
        """Testing deleting the basemodel from the fileStorage"""
        amenities_before = models.storage.all(Amenity)
        i = Amenity(name="TV")
        i.save()
        amenities_after = models.storage.all(Amenity)
        self.assertTrue(len(amenities_after) == len(amenities_before) + 1)
        self.assertIn(i, amenities_after.values())
        i.delete()
        amenities = models.storage.all(Amenity)
        self.assertNotIn("Amenity." + i.id, amenities)
        self.assertNotIn(i, amenities.values())


if __name__ == '__main__':
    unittest.main()
    pass
