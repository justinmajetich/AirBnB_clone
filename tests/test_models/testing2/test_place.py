#!/st/bin/python3
"""Defines unittests for Place.py

Unittests classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place

class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of class: Place"""

    def test_no_args(self):
        self.assertEqual(Place, type(Place()))

    def test_new_gets_stored(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_public_and_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_public_and_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_public_and_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_and_str(self):
        self.assertEqual(str, type(Place.city_id))

    def test_user_id_is_public_and_str(self):
        self.assertEqual(str, type(Place.user_id))

    def test_name_is_public_and_str(self):
        self.assertEqual(str, type(Place.name))

    def test_desc_is_public_and_str(self):
        self.assertEqual(str, type(Place.description))

    def test_number_rooms_is_public_and_int(self):
        self.assertEqual(int, type(Place.number_rooms))

    def test_number_bath_is_public_and_int(self):
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_max_guest_is_public_and_int(self):
        self.assertEqual(int, type(Place.max_guest))

    def test_price_by_night_is_public_and_int(self):
        self.assertEqual(int, type(Place.price_by_night))

    def test_lat_is_public_and_float(self):
        self.assertEqual(float, type(Place.latitude))

    def test_long_is_public_and_float(self):
        self.assertEqual(float, type(Place.longitude))

    def test_amenity_ids_is_public_and_list(self):
        self.assertEqual(list, type(Place.amenity_ids))

    def test_two_Places_ids_unique(self):
        plc1 = Place()
        st2 = Place()
        self.assertNotEqual(plc1.id, st2.id)

    def test_two_Places_diff_created_at(self):
        plc1 = Place()
        sleep(0.1)
        st2 = Place()
        self.assertLess(plc1.created_at, st2.created_at)

    def test_two_Places_diff_updated_at(self):
        plc1 = Place()
        sleep(0.1)
        st2 = Place()
        self.assertLess(plc1.updated_at, st2.updated_at)

    def test_str_value(self):
        d_t = datetime.now()
        d_t_r = repr(d_t)
        plc = Place()
        plc.id = "66566"
        plc.created_at = d_t
        plc.updated_at = d_t
        plc_str = plc.__str__()
        self.assertIn("[Place] (66566)", plc_str)
        self.assertIn("'id': '66566'", plc_str)
        self.assertIn("'created_at': " + d_t_r, plc_str)
        self.assertIn("'updated_at': " + d_t_r, plc_str)

    def test_arguments_not_used(self):
        plc = Place(None)
        self.assertNotIn(None, plc.__dict__.values())

    def test_with_kwargs_None(self):
        with self.assertRaises(TypeError):
            Place(id=None, create_at=None, updated_at=None)

class TestPlace_save(unittest.TestCase):
    """Unittests for save method of class: Place"""

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
        plc = Place()
        sleep(0.1)
        firplc_update = plc.updated_at
        plc.save()
        self.assertLess(firplc_update, plc.updated_at)

    def test_two_saves(self):
        plc = Place()
        sleep(0.1)
        firplc_update = plc.updated_at
        plc.save()
        second_update = plc.updated_at
        self.assertLess(firplc_update, second_update)
        sleep(0.1)
        plc.save()
        self.assertLess(second_update, plc.updated_at)

    def test_save_with_argument(self):
        plc = Place()
        with self.assertRaises(TypeError):
            plc.save(None)

    def test_save_updates_file(self):
        plc = Place()
        plc.save()
        plc_id = "Place." + plc.id
        with open("file.json", "r") as file:
            self.assertIn(plc_id, file.read())

class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of class: Place"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_keys_accurate(self):
        plc = Place()
        self.assertIn("id", plc.to_dict())
        self.assertIn("created_at", plc.to_dict())
        self.assertIn("updated_at", plc.to_dict())
        self.assertIn("__class__", plc.to_dict())

    def test_to_dict_containes_added_attr(self):
        plc = Place()
        plc.middle_nplce = "Ryan"
        plc.meaning = 42
        self.assertEqual("Ryan", plc.middle_nplce)
        self.assertIn("meaning", plc.to_dict())

    def test_to_dict_datetime_is_str(self):
        plc = Place()
        plc_dict = plc.to_dict()
        self.assertEqual(str, type(plc_dict["id"]))
        self.assertEqual(str, type(plc_dict["created_at"]))
        self.assertEqual(str, type(plc_dict["updated_at"]))

    def test_to_dict_out(self):
        d_t = datetime.now()
        plc = Place()
        plc.id = "66566"
        plc.created_at = d_t
        plc.updated_at = d_t
        temp_dict = {
            'id': '66566',
            '__class__': 'Place',
            'created_at': d_t.isoformat(),
            'updated_at': d_t.isoformat()
        }
        self.assertDictEqual(plc.to_dict(), temp_dict)

    def test_to_dict_dunder_dict_diff(self):
        plc = Place()
        self.assertNotEqual(plc.to_dict(), plc.__dict__)

    def test_to_dict_with_argument(self):
        plc = Place()
        with self.assertRaises(TypeError):
            plc.to_dict(None)

if __name__ == "__main__":
    unittest.main()
