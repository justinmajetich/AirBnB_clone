#!/usr/bin/python3
''' Test suite for the console'''


import sys
import unittest
from models import storage
from io import StringIO
from console import HBNBCommand
from os import getenv
import pep8

db = getenv("HBNB_TYPE_STORAGE", "fs")


class test_console(unittest.TestCase):
    ''' Test the console module'''
    def setUp(self):
        '''setup for'''
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        ''''''
        sys.stdout = self.backup

    def create(self):
        ''' create an instance of the HBNBCommand class'''
        return HBNBCommand()

    def test_pep8_console(self):
        """Pep8 console.py"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Kindly fix Pep8')

    def test_quit(self):
        ''' Test quit exists'''
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        ''' Test EOF exists'''
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_all(self):
        ''' Test all exists'''
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    @unittest.skipIf(db == "db", "Testing database storage only")
    def test_show(self):
        '''
            Testing that show exists
        '''
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + user_id)
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertTrue(str is type(x))

    def test_show_class_name(self):
        '''
            Test show message error for id missing
        '''
        console = self.create()
        console.onecmd("create User")
        # user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** instance id missing **\n", x)

    @unittest.skipIf(db == "db", "Testing database storage only")
    def test_show_no_instance_found(self):
        '''
            Test show message error for id missing
        '''
        console = self.create()
        console.onecmd("create User")
        # user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + "1234567898")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n", x)

    def test_create(self):
        '''
            Test that create works
        '''
        console = self.create()
        console.onecmd("create User email=adriel@hbnb.com password=abc")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_class_name(self):
        '''
            Testing the error messages for class name missing.
        '''
        console = self.create()
        console.onecmd("create")
        x = (self.capt_out.getvalue())
        self.assertEqual("** class name missing **\n", x)

    def test_class_name_doest_exist(self):
        '''
            Testing the error messages for class name missing.
        '''
        console = self.create()
        console.onecmd("create Holla")
        x = (self.capt_out.getvalue())
        self.assertEqual("** class doesn't exist **\n", x)

    @unittest.skipIf(db != 'db', "Testing DBstorage only")
    def test_create_db(self):
        console = self.create()
        console.onecmd("create State name=California")
        result = storage.all("State")
        self.assertTrue(len(result) > 0)
