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
        """
            function construct
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        """
            functionn destruct
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    @unittest.skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def testCreateMissingClass(self):
        """
            create() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    @unittest.skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def testInvalidClass(self):
        """
            create() invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    @unittest.skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def testCreateInstance(self):
        """
            create()
        """
        for prmClassName in self.__classes:
            self.__testCreateObject(prmClassName)

    @unittest.skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def testCreateInstanceWithParameter(self):
        """
            create()
        """
        for prmClassName in self.__classes:
            self.__testCreateObjectWithParameter(prmClassName)

    @unittest.skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def testInvalidParameter(self):
        """
            create()
        """
        for prmClassName in self.__classes:
            self.__testCreateObjectWithInvalidParameter(prmClassName)

    @unittest.skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def testWithMixedValidityParameter(self):
        """
            create()
        """
        for prmClassName in self.__classes:
            self.__testMixedValidityParameter(prmClassName)

    @unittest.skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def testWithMixedTypeParameter(self):
        """
            create()
        """
        for prmClassName in self.__classes:
            self.__testMixedTypeParameter(prmClassName)

    @unittest.skipIf(
        os.environ.get('HBNB_ENV') == 'test' and
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def testStringParameterWithUnderscore(self):
        """
            create()
        """
        for prmClassName in self.__classes:
            self.__testStringWithUnderscore(prmClassName)

    def __testCreateObject(self, prmClassName):
        """
            test simple object creation
        """
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
        """
            test object creation with parameter
        """
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

    def __testStringWithUnderscore(self, prmClassName):
        """
            test object creation with a string with underscore
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(
                HBNBCommand().onecmd(
                    "create {} {}={}".format(
                        prmClassName,
                        'name',
                        'My_little_house'
                    )
                )
            )
            id = output.getvalue().strip()
            key = "{}.{}".format(prmClassName, id)
            self.assertIn(key, storage.all().keys())
            obj = self.__getObj(prmClassName, id)
            self.assertIn('name', obj.to_dict())
            self.assertEqual(obj.to_dict()['name'], 'My little house')
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))

    def __testCreateObjectWithInvalidParameter(self, prmClassName):
        """
            test object creation with invalid parameter
        """
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
        """
            test object creation with invalid and valid parameter
        """
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
        """
            test object creation with different type of parameter
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(
                HBNBCommand().onecmd(
                    "create {} {}={} {}={} {}={}".format(
                        prmClassName,
                        'age',
                        3,
                        'name',
                        "California",
                        'latitude',
                        8.6545
                    )
                )
            )
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
        """
            get object from storage
        """
        return storage.all()["{}.{}".format(prmClassName, prmUuid)]
