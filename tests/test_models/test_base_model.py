#!/usr/bin/python3
"""Module that contains unittests for base_model"""
from models.base_model import BaseModel
from datetime import datetime
import unittest
import json
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 'basemodel test not supported')
class test_basemodel(unittest.TestCase):
    """ test class for base_model class"""

    def __init__(self, *args, **kwargs):
        """ init the test class of basemodel"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ the set up method of the test class"""
        pass

    def tearDown(self):
        """the teardown method of the ctest class"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """ default testing of basemodel"""
        var = self.value()
        self.assertEqual(type(var), self.value)

    def test_kwargs(self):
        """ testing basemodel with kwargs"""
        var = self.value()
        copy = var.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is var)

    def test_kwargs_int(self):
        """ testing with kwargs again but with int kwargs"""
        var = self.value()
        copy = var.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)
            self.assertFalse(new is var)

    def test_save(self):
        """ Testing save metthod"""
        var = self.value()
        var.save()
        key = self.name + "." + var.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], var.to_dict())

    def test_str(self):
        """ testing the str method of themodel"""
        var = self.value()
        self.assertEqual(str(var), '[{}] ({}) {}'.format(self.name, var.id,
                         var.__dict__))

    def test_todict(self):
        """ testing the to_dict method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)
        self.assertIsInstance(self.value().to_dict(), dict)
        self.assertIn('id', self.value().to_dict())
        self.assertIn('created_at', self.value().to_dict())
        self.assertIn('updated_at', self.value().to_dict())
        mdl = self.value()
        mdl.firstname = 'Hannibal'
        mdl.lastname = 'Mejbri'
        self.assertIn('firstname', mdl.to_dict())
        self.assertIn('lastname', mdl.to_dict())
        self.assertIn('firstname', self.value(firstname='Hannibal').to_dict())
        self.assertIn('lastname', self.value(lastname='Mejbri').to_dict())
        self.assertIsInstance(self.value().to_dict()['created_at'], str)
        self.assertIsInstance(self.value().to_dict()['updated_at'], str)
        datetime_now = datetime.today()
        mdl = self.value()
        mdl.id = '13'
        mdl.created_at = mdl.updated_at = datetime_now
        to_dict = {
            'id': '13',
            '__class__': mdl.__class__.__name__,
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(mdl.to_dict(), to_dict)
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertDictEqual(
                self.value(id='13', age=22).to_dict(),
                {
                    '__class__': mdl.__class__.__name__,
                    'id': '13',
                    'age': 22
                }
            )
            self.assertDictEqual(
                self.value(id='13', age=None).to_dict(),
                {
                    '__class__': mdl.__class__.__name__,
                    'id': '13',
                    'age': None
                }
            )
        mdl_d = self.value()
        self.assertIn('__class__', self.value().to_dict())
        self.assertNotIn('__class__', self.value().__dict__)
        self.assertNotEqual(mdl_d.to_dict(), mdl_d.__dict__)
        self.assertNotEqual(
            mdl_d.to_dict()['__class__'],
            mdl_d.__class__
        )
        with self.assertRaises(TypeError):
            self.value().to_dict(None)
        with self.assertRaises(TypeError):
            self.value().to_dict(self.value())
        with self.assertRaises(TypeError):
            self.value().to_dict(45)
        self.assertNotIn('_sa_instance_state', n)

    def test_kwargs_none(self):
        """ testing kwargs again with none"""
        nada = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**nada)
            self.assertFalse(new is nada)

    def test_kwargs_one(self):
        """ testing kwargs with one arg"""
        nad = {'name': 'test'}
        new = self.value(**nad)
        self.assertEqual(new.name, nad['name'])

    def test_id(self):
        """ testing id attr of the model"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ testing created at attr"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime)

    def test_updated_at(self):
        """ testing updated at attr"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)