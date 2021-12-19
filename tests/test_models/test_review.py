#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review

import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
from unittest.mock import patch
import pycodestyle
import models


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_pep8_user(self):
        """test pep8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def setup_class(self):
        """Setup for docstring"""
        self.user_1 = Review()

    def test_docstrings(self):
        """test documentation"""
        self.assertIsNotNone(Review.__doc__, "review.py needs a docstring")

    """Test if user inherit from BaseModel"""
    def test_instance(self):
        """check if Review is an instance of BaseModel"""
        user = Review()
        self.assertIsInstance(user, Review)
        self.assertTrue(issubclass(type(user), BaseModel))
        self.assertEqual(str(type(user)), "<class 'models.review.Review'>")

    """Testing Review class"""
    def test_instances(self):
        with patch('models.review'):
            instance = Review()
            self.assertEqual(type(instance), Review)
            instance.place_id = "3344"
            instance.text = "SiliconValley"
            expectec_attrs_types = {
                    "id": str,
                    "created_at": datetime,
                    "updated_at": datetime,
                    "place_id": str,
                    "text": str
                    }
            inst_dict = instance.to_dict()
            expected_dict_attrs = [
                    "id",
                    "created_at",
                    "updated_at",
                    "place_id",
                    "text",
                    "__class__"
                    ]
            self.assertCountEqual(inst_dict.keys(), expected_dict_attrs)
            self.assertEqual(inst_dict['place_id'], '3344')
            self.assertEqual(inst_dict['text'], "SiliconValley")
            self.assertEqual(inst_dict['__class__'], 'Review')

            for attr, types in expectec_attrs_types.items():
                with self.subTest(attr=attr, typ=types):
                    self.assertIn(attr, instance.__dict__)
                    self.assertIs(type(instance.__dict__[attr]), types)
            self.assertEqual(instance.place_id, "3344")
            self.assertEqual(instance.text, "SiliconValley")

    def test_Review_id_and_createat(self):
        """testing id for every user"""
        user_1 = Review()
        sleep(2)
        user_2 = Review()
        sleep(2)
        user_3 = Review()
        sleep(2)
        list_users = [user_1, user_2, user_3]
        for instance in list_users:
            user_id = instance.id
            with self.subTest(user_id=user_id):
                self.assertIs(type(user_id), str)
        self.assertNotEqual(user_1.id, user_2.id)
        self.assertNotEqual(user_1.id, user_3.id)
        self.assertNotEqual(user_2.id, user_3.id)
        self.assertTrue(user_1.created_at <= user_2.created_at)
        self.assertTrue(user_2.created_at <= user_3.created_at)
        self.assertNotEqual(user_1.created_at, user_2.created_at)
        self.assertNotEqual(user_1.created_at, user_3.created_at)
        self.assertNotEqual(user_3.created_at, user_2.created_at)

    def test_str_method(self):
        """
        Testin str magic method
        """
        inst = Review()
        str_output = "[Review] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(str_output, str(inst))

    @patch('models.storage')
    def test_save_method(self, mock_storage):
        """Testing save method and if it update"""
        instance5 = Review()
        created_at = instance5.created_at
        sleep(2)
        updated_at = instance5.updated_at
        instance5.save()
        new_created_at = instance5.created_at
        sleep(2)
        new_updated_at = instance5.updated_at
        self.assertNotEqual(updated_at, new_updated_at)
        self.assertEqual(created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)


if __name__ == '__main__':
    unittest.main()
