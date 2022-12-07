#!/rer/bin/python3
"""Defines unittests for models/Review.py.
Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_str(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_id_is_public_str(self):
        self.assertEqual(str, type(Review.user_id))

    def test_text_is_public_str(self):
        self.assertEqual(str, type(Review.text))

    def test_two_Reviews_unique_ids(self):
        re1 = Review()
        re2 = Review()
        self.assertNotEqual(re1.id, re2.id)

    def test_two_Reviews_different_created_at(self):
        re1 = Review()
        sleep(0.05)
        re2 = Review()
        self.assertLess(re1.created_at, re2.created_at)

    def test_two_Reviews_different_updated_at(self):
        re1 = Review()
        sleep(0.05)
        re2 = Review()
        self.assertLess(re1.updated_at, re2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        re = Review()
        re.id = "123456"
        re.created_at = re.updated_at = dt
        restr = re.__str__()
        self.assertIn("[Review] (123456)", restr)
        self.assertIn("'id': '123456'", restr)
        self.assertIn("'created_at': " + dt_repr, restr)
        self.assertIn("'updated_at': " + dt_repr, restr)

    def test_args_unamed(self):
        re = Review(None)
        self.assertNotIn(None, re.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        re = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(re.id, 345)
        self.assertEqual(re.created_at, dt)
        self.assertEqual(re.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
    """Unittests for testing save method of the  class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        re = Review()
        sleep(0.05)
        first_updated_at = re.updated_at
        re.save()
        self.assertLess(first_updated_at, re.updated_at)

    def test_two_saves(self):
        re = Review()
        sleep(0.05)
        first_updated_at = re.updated_at
        re.save()
        second_updated_at = re.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        re.save()
        self.assertLess(second_updated_at, re.updated_at)

    def test_save_with_arg(self):
        re = Review()
        with self.assertRaises(TypeError):
            re.save(None)

    def test_save_updates_file(self):
        re = Review()
        re.save()
        reid = "Review." + re.id
        with open("file.json", "r") as f:
            self.assertIn(reid, f.read())


class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        re = Review()
        self.assertIn("id", re.to_dict())
        self.assertIn("created_at", re.to_dict())
        self.assertIn("updated_at", re.to_dict())
        self.assertIn("__class__", re.to_dict())

    def test_to_dict_contains_added_attributes(self):
        re = Review()
        re.middle_name = "Holberton"
        re.my_number = 98
        self.assertEqual("Holberton", re.middle_name)
        self.assertIn("my_number", re.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        re = Review()
        re_dict = re.to_dict()
        self.assertEqual(str, type(re_dict["id"]))
        self.assertEqual(str, type(re_dict["created_at"]))
        self.assertEqual(str, type(re_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        re = Review()
        re.id = "123456"
        re.created_at = re.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(re.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        re = Review()
        self.assertNotEqual(re.to_dict(), re.__dict__)

    def test_to_dict_with_arg(self):
        re = Review()
        with self.assertRaises(TypeError):
            re.to_dict(None)


if __name__ == "__main__":
    unittest.main()
