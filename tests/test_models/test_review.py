#!/usr/bin/python3
"""Test cases for Review model"""

import unittest
import os
import models
from time import sleep
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class ReviewTest(unittest.TestCase):
    """Review test cases"""
    def test_Review_inherits_baseModel(self):
        """check that Review inherits from BaseModel"""
        review = Review()
        self.assertTrue(isinstance(review, BaseModel))

    def test_Review_instance_type(self):
        """check the instance's type"""
        review = Review()
        self.assertEqual(type(review), Review)

    def test_Review_id_attr(self):
        """check Review's id attribute is public"""
        review = Review()
        self.assertEqual(str, type(review.id))

    def test_Review_createAt_attr(self):
        """check Review's create_at attribute is public"""
        review = Review()
        self.assertEqual(datetime, type(review.created_at))

    def test_Review_updatedAt_attr(self):
        """check Review's updated_at attribute is public"""
        review = Review()
        self.assertEqual(datetime, type(review.updated_at))

    def test_Review_place_id_attr(self):
        """check Review's place_id attribute is public"""
        review = Review()
        self.assertEqual(str, type(review.place_id))

    def test_Review_user_id_attr(self):
        """check Review's user_id attribute is public"""
        review = Review()
        self.assertEqual(str, type(review.user_id))

    def test_Review_text_attr(self):
        """check Review's text attribute is public"""
        review = Review()
        self.assertEqual(str, type(review.text))

    def test_Review_two_reviews_diffrent_ids(self):
        """check two reviews have diffrent id"""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_Review_init_unused_args(self):
        """check that args are not used"""
        obj1 = Review("val")
        self.assertNotIn("val", obj1.__dict__.values())

    def test_Review_two_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            Review().to_dict("val")


class ReviewSaveTest(unittest.TestCase):
    """test cases for Uer.save() method"""
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "_file.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("_file.json", "file.json")
        except IOError:
            pass

    def test_Review_save_none_arg(self):
        """test save with None arg"""
        obj1 = Review()
        with self.assertRaises(TypeError):
            obj1.save(None)

    def test_Review_save_updatedAt_is_date(self):
        """check if save() saves datetime"""
        obj1 = Review()
        self.assertEqual(type(obj1.updated_at), datetime)

    def test_Review_save_updatedAt_changed(self):
        """check if save() changes the updated_at"""
        obj1 = Review()
        oldDate = obj1.updated_at
        obj1.save()
        newDate = obj1.updated_at
        self.assertTrue(oldDate < newDate)

    def test_Review_save_file_json(self):
        """test if instance is saved in the json file"""
        obj1 = Review()
        obj1.save()
        val = "Review." + obj1.id
        with open("file.json", "r") as file:
            self.assertIn(val, file.read())

    def test_Review_save_file_json_two_instances(self):
        """test if two instances is saved in the json file"""
        obj1 = Review()
        obj2 = Review()
        obj1.save()
        sleep(0.05)
        obj2.save()
        val1 = "Review." + obj1.id
        val2 = "Review." + obj2.id

        with open("file.json", "r") as file:
            self.assertIn(val1, file.read())
        with open("file.json", "r") as file:
            self.assertIn(val2, file.read())


class ReviewToDictTest(unittest.TestCase):
    """test to_dict()"""
    def test_Review_to_dict_vs_dunder_dict(self):
        "check obj.to_dict() is equal to obj.__dict__"
        obj1 = Review()
        self.assertNotEqual(obj1.to_dict(), obj1.__dict__)

    def test_Review_to_dict_with_arg(self):
        """test save with an arg"""
        obj1 = Review()
        with self.assertRaises(TypeError):
            obj1.save("val")

    def test_to_dict_attributes_type_str(self):
        """check if the attributes are strings"""
        obj = Review()
        obj_dict = obj.to_dict()
        self.assertEqual(str, type(obj_dict["id"]))
        self.assertEqual(str, type(obj_dict["created_at"]))
        self.assertEqual(str, type(obj_dict["updated_at"]))

    def test_Review_initialization_with_kwargs(self):
        """check Review when initializated with kwargs"""
        review = Review()
        date = datetime.now()
        review.id = "123-456-78"
        review.created_at = review.updated_at = date
        review.place_id = "place-123"
        review.user_id = "user-123"
        review.text = "text"
        td = {
            "id": "123-456-78",
            "place_id": "place-123",
            "user_id": "user-123",
            "text": "text",
            "created_at": date.isoformat(),
            "updated_at": date.isoformat(),
            "__class__": "Review"
        }
        self.assertDictEqual(review.to_dict(), td)
