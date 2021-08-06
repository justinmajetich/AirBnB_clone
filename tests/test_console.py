#!/usr/bin/python3


from os import system
from models.engine.file_storage import FileStorage
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
import os

class ConsoleCreateTest(unittest.TestCase):
    __classes = [
        'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
    ]

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def testCreateMissingClass(self):
        """
            create() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    def testInvalidClass(self):
        """
            create() invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def testCreateInstance(self):
        """
            create()
        """
        for prmClassName in self.__classes:
            self.__testCreateObject(prmClassName)

    def testCreateInstanceWithParameter(self):
        """
            create()
        """
        for prmClassName in self.__classes:
            self.__testCreateObjectWithParameter(prmClassName)

    def testInvalidParameter(self):
        """
            create()
        """
        for prmClassName in self.__classes:
            self.__testCreateObjectWithInvalidParameter(prmClassName)

    def testWithMixedValidityParameter(self):
        """
            create()
        """
        for prmClassName in self.__classes:
            self.__testMixedValidityParameter(prmClassName)

    def testWithMixedTypeParameter(self):
        """
            create()
        """
        for prmClassName in self.__classes:
            self.__testMixedTypeParameter(prmClassName)

    def __testCreateObject(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
            id = output.getvalue().strip()
            key = "{}.{}".format(prmClassName, id)
            self.assertIn(key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))

    def __testCreateObjectWithParameter(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {} {}={}".format(prmClassName, 'name', 'California')))
            id = output.getvalue().strip()
            key = "{}.{}".format(prmClassName, id)
            self.assertIn(key, storage.all().keys())
            obj = self.__getObj(prmClassName, id)
            self.assertIn('name', obj.to_dict())
            self.assertEqual(obj.to_dict()['name'], 'California')
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))

    def __testCreateObjectWithInvalidParameter(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {} {}".format(prmClassName, 'name')))
            id = output.getvalue().strip()
            key = "{}.{}".format(prmClassName, id)
            self.assertIn(key, storage.all().keys())
            obj = self.__getObj(prmClassName, id)
            self.assertNotIn('name', obj.to_dict())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))
                

    def __testMixedValidityParameter(self, prmClassName):
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {} {} {} {}={}".format(
                    prmClassName, 'name', 'California', 'country', 'USA'
                )
            ))
            id = output.getvalue().strip()
            key = "{}.{}".format(prmClassName, id)
            self.assertIn(key, storage.all().keys())
            obj = self.__getObj(prmClassName, id)
            self.assertIn('country', obj.to_dict())
            self.assertEqual(obj.to_dict()['country'], 'USA')
            self.assertNotIn('name', obj.to_dict())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))
            

    def __testMixedTypeParameter(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {} {}={} {}={} {}={}".format(prmClassName, 'age', 3, 'name', "California", 'latitude', 8.6545)))
            id = output.getvalue().strip()
            key = "{}.{}".format(prmClassName, id)
            self.assertIn(key, storage.all().keys())
            obj = self.__getObj(prmClassName, id)
            self.assertIn('age', obj.to_dict())
            self.assertEqual(obj.to_dict()['age'], 3)
            self.assertIn('name', obj.to_dict())
            self.assertEqual(obj.to_dict()['name'], 'California')
            self.assertIn('latitude', obj.to_dict())
            self.assertEqual(obj.to_dict()['latitude'], 8.6545)
            self.assertIsInstance(obj.age, int)
            self.assertIsInstance(obj.name, str)
            self.assertIsInstance(obj.latitude, float)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))

    def __getObj(self, prmClassName: str, prmUuid: str):
        return storage.all()["{}.{}".format(prmClassName, prmUuid)]
