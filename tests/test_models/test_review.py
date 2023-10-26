#!/st/bin/python3
"""Defines unittests for Review.py

Unittests classes:
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
    """Unittests for testing instantiation of class: Review"""

    def test_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_new_gets_stored(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_public_and_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_public_and_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_public_and_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_and_str(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_id_is_public_and_str(self):
        self.assertEqual(str, type(Review.user_id))

    def test_text_is_public_and_str(self):
        self.assertEqual(str, type(Review.text))

    def test_two_Reviews_ids_unique(self):
        rev1 = Review()
        st2 = Review()
        self.assertNotEqual(rev1.id, st2.id)

    def test_two_Reviews_diff_created_at(self):
        rev1 = Review()
        sleep(0.1)
        st2 = Review()
        self.assertLess(rev1.created_at, st2.created_at)

    def test_two_Reviews_diff_updated_at(self):
        rev1 = Review()
        sleep(0.1)
        st2 = Review()
        self.assertLess(rev1.updated_at, st2.updated_at)

    def test_str_value(self):
        d_t = datetime.now()
        d_t_r = repr(d_t)
        rev = Review()
        rev.id = "66566"
        rev.created_at = d_t
        rev.updated_at = d_t
        rev_str = rev.__str__()
        self.assertIn("[Review] (66566)", rev_str)
        self.assertIn("'id': '66566'", rev_str)
        self.assertIn("'created_at': " + d_t_r, rev_str)
        self.assertIn("'updated_at': " + d_t_r, rev_str)

    def test_arguments_not_used(self):
        rev = Review(None)
        self.assertNotIn(None, rev.__dict__.values())

    def test_with_kwargs_None(self):
        with self.assertRaises(TypeError):
            Review(id=None, create_at=None, updated_at=None)

class TestReview_save(unittest.TestCase):
    """Unittests for save method of class: Review"""

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
        rev = Review()
        sleep(0.1)
        firrev_update = rev.updated_at
        rev.save()
        self.assertLess(firrev_update, rev.updated_at)

    def test_two_saves(self):
        rev = Review()
        sleep(0.1)
        firrev_update = rev.updated_at
        rev.save()
        second_update = rev.updated_at
        self.assertLess(firrev_update, second_update)
        sleep(0.1)
        rev.save()
        self.assertLess(second_update, rev.updated_at)

    def test_save_with_argument(self):
        rev = Review()
        with self.assertRaises(TypeError):
            rev.save(None)

    def test_save_updates_file(self):
        rev = Review()
        rev.save()
        rev_id = "Review." + rev.id
        with open("file.json", "r") as file:
            self.assertIn(rev_id, file.read())

class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of class: Review"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_keys_accurate(self):
        rev = Review()
        self.assertIn("id", rev.to_dict())
        self.assertIn("created_at", rev.to_dict())
        self.assertIn("updated_at", rev.to_dict())
        self.assertIn("__class__", rev.to_dict())

    def test_to_dict_containes_added_attr(self):
        rev = Review()
        rev.middle_nreve = "Ryan"
        rev.meaning = 42
        self.assertEqual("Ryan", rev.middle_nreve)
        self.assertIn("meaning", rev.to_dict())

    def test_to_dict_datetime_is_str(self):
        rev = Review()
        rev_dict = rev.to_dict()
        self.assertEqual(str, type(rev_dict["id"]))
        self.assertEqual(str, type(rev_dict["created_at"]))
        self.assertEqual(str, type(rev_dict["updated_at"]))

    def test_to_dict_out(self):
        d_t = datetime.now()
        rev = Review()
        rev.id = "66566"
        rev.created_at = d_t
        rev.updated_at = d_t
        temp_dict = {
            'id': '66566',
            '__class__': 'Review',
            'created_at': d_t.isoformat(),
            'updated_at': d_t.isoformat()
        }
        self.assertDictEqual(rev.to_dict(), temp_dict)

    def test_to_dict_dunder_dict_diff(self):
        rev = Review()
        self.assertNotEqual(rev.to_dict(), rev.__dict__)

    def test_to_dict_with_argument(self):
        rev = Review()
        with self.assertRaises(TypeError):
            rev.to_dict(None)

if __name__ == "__main__":
    unittest.main()
