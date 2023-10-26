#!/st/bin/python3
"""Defines unittests for City.py

Unittests classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of class: City"""

    def test_no_args(self):
        self.assertEqual(City, type(City()))

    def test_new_gets_stored(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_public_and_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_public_and_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_public_and_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_name_is_public_and_str(self):
        self.assertEqual(str, type(City.name))
        self.assertEqual(str, type(City.state_id))

    def test_two_Citys_ids_unique(self):
        cty1 = City()
        st2 = City()
        self.assertNotEqual(cty1.id, st2.id)

    def test_two_Citys_diff_created_at(self):
        cty1 = City()
        sleep(0.1)
        st2 = City()
        self.assertLess(cty1.created_at, st2.created_at)

    def test_two_Citys_diff_updated_at(self):
        cty1 = City()
        sleep(0.1)
        st2 = City()
        self.assertLess(cty1.updated_at, st2.updated_at)

    def test_str_value(self):
        d_t = datetime.now()
        d_t_r = repr(d_t)
        cty = City()
        cty.id = "66566"
        cty.created_at = d_t
        cty.updated_at = d_t
        cty_str = cty.__str__()
        self.assertIn("[City] (66566)", cty_str)
        self.assertIn("'id': '66566'", cty_str)
        self.assertIn("'created_at': " + d_t_r, cty_str)
        self.assertIn("'updated_at': " + d_t_r, cty_str)

    def test_arguments_not_used(self):
        cty = City(None)
        self.assertNotIn(None, cty.__dict__.values())

    def test_with_kwargs_None(self):
        with self.assertRaises(TypeError):
            City(id=None, create_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for save method of class: City"""

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
        cty = City()
        sleep(0.1)
        fircty_update = cty.updated_at
        cty.save()
        self.assertLess(fircty_update, cty.updated_at)

    def test_two_saves(self):
        cty = City()
        sleep(0.1)
        fircty_update = cty.updated_at
        cty.save()
        second_update = cty.updated_at
        self.assertLess(fircty_update, second_update)
        sleep(0.1)
        cty.save()
        self.assertLess(second_update, cty.updated_at)

    def test_save_with_argument(self):
        cty = City()
        with self.assertRaises(TypeError):
            cty.save(None)

    def test_save_updates_file(self):
        cty = City()
        cty.save()
        cty_id = "City." + cty.id
        with open("file.json", "r") as file:
            self.assertIn(cty_id, file.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of class: City"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_keys_accurate(self):
        cty = City()
        self.assertIn("id", cty.to_dict())
        self.assertIn("created_at", cty.to_dict())
        self.assertIn("updated_at", cty.to_dict())
        self.assertIn("__class__", cty.to_dict())

    def test_to_dict_containes_added_attr(self):
        cty = City()
        cty.middle_nctye = "Ryan"
        cty.meaning = 42
        self.assertEqual("Ryan", cty.middle_nctye)
        self.assertIn("meaning", cty.to_dict())

    def test_to_dict_datetime_is_str(self):
        cty = City()
        cty_dict = cty.to_dict()
        self.assertEqual(str, type(cty_dict["id"]))
        self.assertEqual(str, type(cty_dict["created_at"]))
        self.assertEqual(str, type(cty_dict["updated_at"]))

    def test_to_dict_out(self):
        d_t = datetime.now()
        cty = City()
        cty.id = "66566"
        cty.created_at = d_t
        cty.updated_at = d_t
        temp_dict = {
            'id': '66566',
            '__class__': 'City',
            'created_at': d_t.isoformat(),
            'updated_at': d_t.isoformat()
        }
        self.assertDictEqual(cty.to_dict(), temp_dict)

    def test_to_dict_dunder_dict_diff(self):
        cty = City()
        self.assertNotEqual(cty.to_dict(), cty.__dict__)

    def test_to_dict_with_argument(self):
        cty = City()
        with self.assertRaises(TypeError):
            cty.to_dict(None)


if __name__ == "__main__":
    unittest.main()



