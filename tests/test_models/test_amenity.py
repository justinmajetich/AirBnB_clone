#!/st/bin/python3
"""Defines unittests for Amenity.py

Unittests classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity

class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of class: Amenity"""

    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_gets_stored(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_public_and_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_public_and_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_public_and_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_and_str(self):
        self.assertEqual(str, type(Amenity.name))

    def test_two_Amenitys_ids_unique(self):
        am1 = Amenity()
        st2 = Amenity()
        self.assertNotEqual(am1.id, st2.id)

    def test_two_Amenitys_diff_created_at(self):
        am1 = Amenity()
        sleep(0.1)
        st2 = Amenity()
        self.assertLess(am1.created_at, st2.created_at)

    def test_two_Amenitys_diff_updated_at(self):
        am1 = Amenity()
        sleep(0.1)
        st2 = Amenity()
        self.assertLess(am1.updated_at, st2.updated_at)

    def test_str_value(self):
        d_t = datetime.now()
        d_t_r = repr(d_t)
        am = Amenity()
        am.id = "66566"
        am.created_at = d_t
        am.updated_at = d_t
        am_str = am.__str__()
        self.assertIn("[Amenity] (66566)", am_str)
        self.assertIn("'id': '66566'", am_str)
        self.assertIn("'created_at': " + d_t_r, am_str)
        self.assertIn("'updated_at': " + d_t_r, am_str)

    def test_arguments_not_used(self):
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_with_kwargs_None(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, create_at=None, updated_at=None)

class TestAmenity_save(unittest.TestCase):
    """Unittests for save method of class: Amenity"""

    @classmethod
    def setup(self):
        try:
            os.rename("file.json", "other")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("other", "file.json")
        except IOError:
            pass

    def test_single_save(self):
        am = Amenity()
        sleep(0.1)
        firam_update = am.updated_at
        am.save()
        self.assertLess(firam_update, am.updated_at)

    def test_two_saves(self):
        am = Amenity()
        sleep(0.1)
        firam_update = am.updated_at
        am.save()
        second_update = am.updated_at
        self.assertLess(firam_update, second_update)
        sleep(0.1)
        am.save()
        self.assertLess(second_update, am.updated_at)

    def test_save_with_argument(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updates_file(self):
        am = Amenity()
        am.save()
        am_id = "Amenity." + am.id
        with open("file.json", "r") as file:
            self.assertIn(am_id, file.read())

class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of class: Amenity"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_keys_accurate(self):
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_to_dict_containes_added_attr(self):
        am = Amenity()
        am.middle_name = "Ryan"
        am.meaning = 42
        self.assertEqual("Ryan", am.middle_name)
        self.assertIn("meaning", am.to_dict())

    def test_to_dict_datetime_is_str(self):
        am = Amenity()
        am_dict = am.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_out(self):
        d_t = datetime.now()
        am = Amenity()
        am.id = "66566"
        am.created_at = d_t
        am.updated_at = d_t
        temp_dict = {
            'id': '66566',
            '__class__': 'Amenity',
            'created_at': d_t.isoformat(),
            'updated_at': d_t.isoformat()
        }
        self.assertDictEqual(am.to_dict(), temp_dict)

    def test_to_dict_dunder_dict_diff(self):
        am = Amenity()
        self.assertNotEqual(am.to_dict(), am.__dict__)

    def test_to_dict_with_argument(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)

if __name__ == "__main__":
    unittest.main()
