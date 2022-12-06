#!/usr/bin/python3
""" Unittest test cases for 'models.base_model' """
import unittest
from models.base_model import BaseModel
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ Test the instantiation of the BaseModel class. """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.model = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        """ """
        try:
<<<<<<< HEAD
            del self.model
        except BaseException:
=======
<<<<<<< HEAD
            os.remove('file.json')
        except:
=======
            del self.model
        except BaseException:
>>>>>>> e3800d5 (Update class models)
>>>>>>> origin/chalo
            pass

    def test_instanceNotNone(self):
        """ """
        self.assertIsNotNone(self.model)

    def test_default(self):
        """ """
        i = self.model()
        self.assertEqual(type(i), self.model)

    def test_assigned_attributes(self):
        """ """
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_type(self):
        """ """
        self.assertIsInstance(self.model.id, str)

    def test_unique_ids(self):
        """ """
        my_model = BaseModel()
        self.assertNotEqual(self.model.id, my_model.id)

    def test_created_at_type(self):
        """ """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        """ """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_creation_time(self):
        """ """
        my_model = self.model()
        self.assertNotEqual(self.model.created_at, my_model.created_at)

    def test_update_time(self):
        """ """
        my_model = self.model()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_no_args_instantiation(self):
        """ """
        self.assertIsInstance(self.model, BaseModel)

    def test_args_instantiation(self):
        """ """
        my_model = BaseModel("name", "number")
        self.assertIsInstance(my_model, BaseModel)

    def test_no_kwargs_instantiation(self):
        """ """
        self.assertIsInstance(self.model, BaseModel)

    def test_kwargs_instantiation(self):
        """ """
        my_model = BaseModel(name="My First Model", number=89)
        self.assertTrue(hasattr(my_model, 'name'))
        self.assertTrue(hasattr(my_model, 'number'))

    def test_kwargs_output(self):
        """ """
        i = self.model()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.model()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.model(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.model(**n)

    """ Test cases for public instance method '__str__()' """

    def test_output_type(self):
        """ """
        self.assertIsNotNone(self.model.__str__())
        self.assertIsInstance(self.model.__str__(), str)

    def test_contains_class_name(self):
        """" """
        self.assertTrue(
            self.model.__str__().__contains__(
                self.model.__class__.__name__
            )
        )

    def test_contains_id(self):
        """ """
        self.assertTrue(
            self.model.__str__().__contains__(self.model.id)
        )

    def test_contains__dict__(self):
        """ """
        self.assertTrue(self.model.__str__().__contains__("id"))
        self.assertTrue(self.model.__str__().__contains__("created_at"))
        self.assertTrue(self.model.__str__().__contains__("updated_at"))

    def test_output_contents(self):
        """ """
        i = self.model()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                                                       i.__dict__))

    def test_without_args(self):
        """ """
        self.assertIsInstance(self.__str__(), str)

    def test_with_args(self):
        """ """
        with self.assertRaises(TypeError):
            self.model.__str__("id")

    """ Test cases for public instance method 'save()' """

    def test_output_type(self):
        """ """
        self.assertIsNone(self.model.save())

    def test_save(self):
        """ Testing save """
        i = self.model()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_updated_at_type(self):
        """ """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_update_time(self):
        """ """
        updated_time = self.model.updated_at
        self.model.save()
        self.assertGreater(self.model.updated_at, updated_time)

    def test_without_args(self):
        """ """
        self.assertIsNone(self.model.save())

    def test_with_args(self):
        """ """
        with self.assertRaises(TypeError):
            self.model.save("id")

    """ Test the `to_dict` instance method of the BaseModel class."""

    def test_output_type(self):
        """ """
        self.assertIsInstance(self.model.to_dict(), dict)

    def test_output_contents(self):
        """ """
        model_json = self.model.to_dict()
        self.assertDictEqual(model_json,
                             {
                                 'id': self.model.id,
                                 'created_at':
                                 self.model.created_at.isoformat(
                                     timespec="microseconds"),
                                 'updated_at':
                                 self.model.updated_at.isoformat(
                                     timespec="microseconds"),
                                 'name': self.model.name,
                                 'number': self.model.number,
                                 '__class__': BaseModel.__name__
                             })

    def test_todict(self):
        """ """
        i = self.model()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_date_format(self):
        """ """
        model_json = self.model.to_dict()
        self.assertIsInstance(model_json['created_at'], str)
        self.assertIsInstance(model_json['updated_at'], str)

    def test_others_type(self):
        """ """
        model_json = self.model.to_dict()
        self.assertIsInstance(model_json['id'], str)
        self.assertIsInstance(model_json['__class__'], str)

    def test_without_args(self):
        """ """
        self.assertIsInstance(self.model.to_dict(), dict)

    def test_with_args(self):
        """ """
        with self.assertRaises(TypeError):
            self.model.to_dict("id")


if __name__ == '__main__':
    unittest.main()
