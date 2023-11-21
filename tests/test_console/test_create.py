#!/usr/bin/env python3
"""test the functioality of the HBNBCommand.create module"""

import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage

class TestCreateCommand(unittest.TestCase):
    """contains the tests to test various functionalities"""
    def setUp(self):
        self.cli = HBNBCommand()

    def test_create_with_params(self):
        """tests object creation with valid params"""
        self.cli.onecmd('create BaseModel name="John_Doe" age=30')
        objects = storage.all()
        for obj in objects.values():
            if isinstance(obj, BaseModel):
                self.assertEqual(obj.name, "John Doe")
                self.assertEqual(obj.age, 30)
                break
        else:
            self.fail("No BaseModel instance found")

    def test_create_with_invalid_params(self):
        """tests obejct creation with invalid params"""
        self.cli.onecmd('create BaseModel invalid_param')
        objects = storage.all()
        for obj in objects.values():
            if isinstance(obj, BaseModel):
                self.assertFalse(hasattr(obj, 'invalid_param'))
                break
            self.fail("No BaseModel instance found")

if __name__ == '__main__':
    unittest.main()
