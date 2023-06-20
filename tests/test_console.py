#!/usr/bin/env python3
"""
This test files holds all the tests needed to test the console application
"""
import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
import re


class TestConsole(unittest.TestCase):
    """
    A unit test to see if the overall functinalits
    of the console like, the precmd, the parsing, the
    excution, unkown command handling, and so on are working
    """
    pass


class TestCreate(unittest.TestCase):
    """
    A unit test class to thest all the create functionalities
    of the create console command.
    """

    def test_create_noArgs(self):
        """
        Tests the create method the one with out no arguments
        """

        with patch('sys.stdout', new=StringIO()) as out_put:
            HBNBCommand().onecmd("create")
        clean_output = out_put.getvalue()
        self.assertEqual(clean_output, "** class name missing **\n")

    def test_create_unExistingClass(self):
        """
        Tests the creat method when the class to be created doesn't
        exist.
        """

        with patch('sys.stdout', new=StringIO()) as out_put:
            HBNBCommand().onecmd("create NOCLASS")
        clean_output = out_put.getvalue()
        self.assertEqual(clean_output, "** class doesn't exist **\n")

    def test_create_withclassName(self):
        """
        Tests the create method with a correcet class name
        """

        with patch('sys.stdout', new=StringIO()) as out_put:
            HBNBCommand().onecmd("create User")
        clean_output = out_put.getvalue()
        # check if the printed value is something like an id
        self.assertRegex(clean_output, r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\n")
        # see if this created object is stored in the file.json
        with open("file.json", "r") as storage:
            db = storage.read()
            # check if the data is stored correclt in the file storage
            result = re.findall("User."+clean_output[:-1], db)
            self.assertTrue(len(result) == 1)
        # do some more test with other class names

    def test_create_classWithOneParams(self):
        """
        Test the create method with paramaetrs
        """

        # delete the database to avoid conflicting
        # names
        from models import storage as f_storage
        f_storage.empty()

        with patch('sys.stdout', new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place name=\"California\"")
        clean_output = out_put.getvalue()
        self.assertRegex(clean_output, r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\n")
        # see if this created object is stored in the file.json
        with open("file.json", "r") as storage:
            db = storage.read()
            # check if the data is stored correclt in the file storage
            result = re.findall("Place."+clean_output[:-1], db)
            self.assertTrue(len(result) == 1)

            result = re.findall("\"name\": \"California\"", db)
            self.assertTrue(len(result) == 1)
        # do some more test with other class names

    def test_create_classWithMoreParams(self):
        """
        Test the create method with paramaetrs
        """

        # delete the database to avoid conflicting
        # names
        from models import storage as f_storage
        f_storage.empty()

        with patch('sys.stdout', new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place name=\"California\
                    " city_id=\"0001\" user_id=\"0001\"")

        clean_output = out_put.getvalue()
        self.assertRegex(clean_output, r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\n")
        # see if this created object is stored in the file.json
        with open("file.json", "r") as storage:
            db = storage.read()
            # check if the data is stored correclt in the file storage
            result = re.findall("Place."+clean_output[:-1], db)
            self.assertTrue(len(result) == 1)

            result = re.findall("\"name\": \"California\"", db)
            self.assertTrue(len(result) == 1)

            result = re.findall("\"city_id\": \"0001\"", db)
            self.assertTrue(len(result) == 1)

            result = re.findall("\"user_id\": \"0001\"", db)
            self.assertTrue(len(result) == 1)
        # do some more test with other class names

    def test_create_valueTypesStrWithDoubleQuote(self):
        """
        Test the create method with paramaetrs that have a string value
        """

        # delete the database to avoid conflicting
        # names
        from models import storage as f_storage
        f_storage.empty()

        with patch('sys.stdout', new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place name=\"Double_quote_Insid\"e\"")
        clean_output = out_put.getvalue()

        self.assertRegex(clean_output, r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\n")
        # see if this created object is stored in the file.json
        with open("file.json", "r") as storage:
            db = storage.read()
            # check if the data is stored correclt in the file storage
            result = re.findall("Place."+clean_output[:-1], db)
            self.assertTrue(len(result) == 1)

            result = re.findall(r'"name": "Double quote Insid\\"e"', db)
            self.assertTrue(len(result) == 1)
        # do some more test with other class names

    def test_create_valueTypeStrWithSpace(self):
        """
        Test the create method with paramaetrs that have a string value
        """

        # delete the database to avoid conflicting
        # names
        from models import storage as f_storage
        f_storage.empty()

        with patch('sys.stdout', new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place name=\"my_little_house\"")
        clean_output = out_put.getvalue()

        self.assertRegex(clean_output, r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\n")
        # see if this created object is stored in the file.json
        with open("file.json", "r") as storage:
            db = storage.read()
            # check if the data is stored correclt in the file storage
            result = re.findall("Place."+clean_output[:-1], db)
            self.assertTrue(len(result) == 1)

            result = re.findall("\"name\": \"my little house\"", db)
            self.assertTrue(len(result) == 1)
        # do some more test with other class names

    def test_create_valueTypeFloat(self):
        """
        Test the create method with paramaetrs that have a string value
        """

        # delete the database to avoid conflicting
        # names
        from models import storage as f_storage
        f_storage.empty()

        with patch('sys.stdout', new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place name=15.6")
        clean_output = out_put.getvalue()

        self.assertRegex(clean_output, r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\n")
        # see if this created object is stored in the file.json
        with open("file.json", "r") as storage:
            db = storage.read()
            # check if the data is stored correclt in the file storage
            result = re.findall("Place."+clean_output[:-1], db)
            self.assertTrue(len(result) == 1)

            result = re.findall("\"name\": 15.6", db)
            self.assertTrue(len(result) == 1)

    def test_create_valueTypeInt(self):
        """
        Test the create method with paramaetrs that have a string value
        """
        # delete the database to avoid conflicting
        # names
        from models import storage as f_storage
        f_storage.empty()

        with patch('sys.stdout', new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place name=15")
        clean_output = out_put.getvalue()

        self.assertRegex(clean_output, r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\n")
        # see if this created object is stored in the file.json
        with open("file.json", "r") as storage:
            db = storage.read()
            # check if the data is stored correclt in the file storage
            result = re.findall("Place."+clean_output[:-1], db)
            self.assertTrue(len(result) == 1)

            result = re.findall("\"name\": 15", db)
            self.assertTrue(len(result) == 1)

    def test_create_valueTypeWrong(self):
        """
        Test the create method with paramaetrs that have a string value
        """
        # delete the database to avoid conflicting
        # names
        from models import storage as f_storage
        f_storage.empty()

        with patch('sys.stdout', new=StringIO()) as out_put:
            HBNBCommand().onecmd("create Place name=_15")
        clean_output = out_put.getvalue()

        self.assertRegex(clean_output, r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\n")
        # see if this created object is stored in the file.json
        with open("file.json", "r") as storage:
            db = storage.read()
            # check if the data is stored correclt in the file storage
            result = re.findall("Place."+clean_output[:-1], db)
            self.assertTrue(len(result) == 1)

            result = re.findall("\"name\": \"_15\"", db)
            self.assertTrue(len(result) == 0)


class TestShow(unittest.TestCase):
    """Test show"""
    pass
