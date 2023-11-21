#!/usr/bin/python3
"""
This module contains all unittests for all console.py features
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import sys
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage


class TestHBNBCommandConsole(unittest.TestCase):
    """
    This contains all tests cases for the Command Console
    """

    def setUp(self):
        """Setup for each tests """
        pass

    def tearDown(self):
        """Tear down after each test case"""
        try:
            os.remove('file.json')
        except Exception as e:
            pass

    def test_help_quit(self):
        """
        Checks if it prints out the right message for help quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            output = f.getvalue()
            expected_output = "Exits the program with formatting\n\n"
            self.assertEqual(output, expected_output)

    def test_help_EOF(self):
        """
        Checks if it prints out the right message for help quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            output = f.getvalue()
            expected_output = "Exits the program without formatting\n\n"
            self.assertEqual(output, expected_output)

    def test_quit(self):
        """
        Checks if quit command returns True
        """
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """
        Checks if EOF command returns True
        """
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_empty_line(self):
        """
        Checks if emptyline works
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            output = f.getvalue()
            expected_output = ""
            self.assertEqual(output, expected_output)

    @unittest.skip("not supported in this version")
    def test_create(self):
        """
        Checks that the  create returns the model id, checks length of id,
        and checks if the file was created
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State')
            output = f.getvalue()
            self.assertTrue(type(output) is str)
            output = output.replace('-', '').replace('\n', '')
            self.assertTrue(len(output) == 32)
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_create_with_params(self):
        """
        Checks that the  create returns the model id, checks length of id,
        and checks if the file was created
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
            output = f.getvalue()
            self.assertTrue(type(output) is str)
            output = output.replace('-', '').replace('\n', '')
            self.assertTrue(len(output) == 32)
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_create_with_invalid_params(self):
        """
        Checks that the  create returns the model id, checks length of id,
        and checks if the file was created
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name=California')
            output = f.getvalue()
            self.assertTrue(type(output) is str)
            output = output.replace('-', '').replace('\n', '')
            self.assertTrue(len(output) == 32)
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_create_non_existent_class(self):
        """
        Checks error management for create command:
        Checks for non-existent class
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create NonexistentClass")
            output = f.getvalue()
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(output, expected_output)

    def test_create_class_name_missing(self):
        """
        Checks error management for create command: Checks class was typed
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue()
            expected_output = "** class name missing **\n"
            self.assertEqual(output, expected_output)

    def test_show(self):
        """
        Checks that the show command works as expected
        """
        inst = User()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show User {inst.id}')
            output = f.getvalue()
            expected_output = str(inst) + '\n'
            self.assertEqual(output, expected_output)

    def test_show_class_name_missing(self):
        """
        Checks error management for show command: No class name entered
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue()
            expected_output = "** class name missing **\n"
            self.assertEqual(output, expected_output)

    def test_show_non_existent_class_name(self):
        """
        Checks error management for show command: Non existent class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show NonexistentClass")
            output = f.getvalue()
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(output, expected_output)

    def test_show_instance_id_missing(self):
        """
        Checks error management for show command: No id entered
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            output = f.getvalue()
            expected_output = "** instance id missing **\n"
            self.assertEqual(output, expected_output)

    def test_show_no_instance_found(self):
        """
        Checks error management for show command: No instance match id
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 57584939")
            output = f.getvalue()
            expected_output = "** no instance found **\n"
            self.assertEqual(output, expected_output)

    def test_destroy(self):
        """
        Checks that the destroy command works as expected
        """
        inst = City()
        self.assertIn(f'City.{inst.id}', storage.all())

        HBNBCommand().onecmd(f'destroy City {inst.id}')
        self.assertNotIn(f'City.{inst.id}', storage.all())

        # Check that 'destroy' saves to file
        with open(storage._FileStorage__file_path, 'r') as f:
            self.assertNotIn(f'User.{inst.id}', f.read())

    def test_destroy_missing_class_name(self):
        """
        Checks error management for destroy command: class name not entered
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue()
            expected_output = "** class name missing **\n"
            self.assertEqual(output, expected_output)

    def test_destroy_non_existent_class(self):
        """
        Checks error management for destroy command: Class name not found
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy NonexistentClass")
            output = f.getvalue()
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(output, expected_output)

    def test_destroy_instance_id_missing(self):
        """
        Checks error management for destroy command: No id entered
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            output = f.getvalue()
            expected_output = "** instance id missing **\n"
            self.assertEqual(output, expected_output)

    def test_destroy_no_instance_found(self):
        """
        Check error management for destroy command:
        no match of instance with id
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 57584939")
            output = f.getvalue()
            expected_output = "** no instance found **\n"
            self.assertEqual(output, expected_output)

    def test_count_base_model(self):
        """
        Checks that count command returns the number of models present
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().precmd("BaseModel.count()")
            output = f.getvalue()
            expected_output = output
            self.assertEqual(output, expected_output)

    def test_count_user(self):
        """
        Checks that count command returns the number of models present
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().precmd("User.count()")
            output = f.getvalue()
            expected_output = output
            self.assertEqual(output, expected_output)

    def test_count_place(self):
        """
        Checks that count command returns the number of models present
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().precmd("Place.count()")
            output = f.getvalue()
            expected_output = output
            self.assertEqual(output, expected_output)

    def test_count_city(self):
        """
        Checks that count command returns the number of models present
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().precmd("City.count()")
            output = f.getvalue()
            expected_output = output
            self.assertEqual(output, expected_output)

    def test_count_state(self):
        """
        Checks that count command returns the number of models present
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().precmd("State.count()")
            output = f.getvalue()
            expected_output = output
            self.assertEqual(output, expected_output)

    def test_count_amenity(self):
        """
        Checks that count command returns the number of models present
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().precmd("Amenity.count()")
            output = f.getvalue()
            expected_output = output
            self.assertEqual(output, expected_output)

    def test_count_review(self):
        """
        Checks that count command returns the number of models present
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().precmd("Review.count()")
            output = f.getvalue()
            expected_output = output
            self.assertEqual(output, expected_output)

    def test_all_user(self):
        """
        Checks that the all User command works as expected
        """
        inst1 = User()
        inst2 = Place()
        inst3 = Amenity()
        inst4 = State()
        inst5 = Review()
        inst6 = City()
        inst7 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().precmd("User.all()")
            output = f.getvalue().replace('\n', '')
            f.truncate(0)
            HBNBCommand().onecmd('all')
            output2 = f.getvalue().replace('\x00', '').replace('\n', '')
        self.assertTrue(output != output2)

    def test_all_place(self):
        """
        Checks that the all Place command works as expected
        """
        inst1 = User()
        inst2 = Place()
        inst3 = Amenity()
        inst4 = State()
        inst5 = Review()
        inst6 = City()
        inst7 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().precmd("Place.all()")
            output = f.getvalue().replace('\n', '')
            f.truncate(0)
            HBNBCommand().onecmd('all')
            output2 = f.getvalue().replace('\x00', '').replace('\n', '')
        self.assertTrue(output != output2)

    def test_all_amenity(self):
        """
        Checks that the all Amenity command works as expected
        """
        inst1 = User()
        inst2 = Place()
        inst3 = Amenity()
        inst4 = State()
        inst5 = Review()
        inst6 = City()
        inst7 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().precmd("Amenity.all()")
            output = f.getvalue().replace('\n', '')
            f.truncate(0)
            HBNBCommand().onecmd('all')
            output2 = f.getvalue().replace('\x00', '').replace('\n', '')
        self.assertTrue(output != output2)

    def test_all_state(self):
        """
        Checks that the all State command works as expected
        """
        inst1 = User()
        inst2 = Place()
        inst3 = Amenity()
        inst4 = State()
        inst5 = Review()
        inst6 = City()
        inst7 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().precmd("State.all()")
            output = f.getvalue().replace('\n', '')
            f.truncate(0)
            HBNBCommand().onecmd('all')
            output2 = f.getvalue().replace('\x00', '').replace('\n', '')
        self.assertTrue(output != output2)

    def test_all_review(self):
        """
        Checks that the all Review command works as expected
        """
        inst1 = User()
        inst2 = Place()
        inst3 = Amenity()
        inst4 = State()
        inst5 = Review()
        inst6 = City()
        inst7 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().precmd("Review.all()")
            output = f.getvalue().replace('\n', '')
            f.truncate(0)
            HBNBCommand().onecmd('all')
            output2 = f.getvalue().replace('\x00', '').replace('\n', '')
        self.assertTrue(output != output2)

    def test_all_city(self):
        """
        Checks that the all City command works as expected
        """
        inst1 = User()
        inst2 = Place()
        inst3 = Amenity()
        inst4 = State()
        inst5 = Review()
        inst6 = City()
        inst7 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().precmd("City.all()")
            output = f.getvalue().replace('\n', '')
            f.truncate(0)
            HBNBCommand().onecmd('all')
            output2 = f.getvalue().replace('\x00', '').replace('\n', '')
        self.assertTrue(output != output2)

    def test_all_base_model(self):
        """
        Checks that the all BaseModel command works as expected
        """
        inst1 = User()
        inst2 = Place()
        inst3 = Amenity()
        inst4 = State()
        inst5 = Review()
        inst6 = City()
        inst7 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().precmd("BaseModel.all()")
            output = f.getvalue().replace('\n', '')
            f.truncate(0)
            HBNBCommand().onecmd('all')
            output2 = f.getvalue().replace('\x00', '').replace('\n', '')
        self.assertTrue(output != output2)

    def test_all_non_existent_class(self):
        """
        Checks error management for all command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all NonexistentClass")
            output = f.getvalue()
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(output, expected_output)

    def test_update(self):
        """
        Checks that the update command works as expected
        """
        inst = Place()
        HBNBCommand().onecmd(f'update Place {inst.id} name "Offal"')
        self.assertTrue(inst.name == 'Offal')
        update_dict = {"name": "Court"}

        # check that attributes can be updated by passing a dict
        f_cmd = f'Place.update({inst.id}, {update_dict})'
        cmd_str = HBNBCommand().precmd(f_cmd)
        HBNBCommand().onecmd(cmd_str)
        self.assertEqual(inst.name, 'Court')

    def test_update_missing_class_name(self):
        """
        Checks error management for update command: class name not entered
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            output = f.getvalue()
            expected_output = "** class name missing **\n"
            self.assertEqual(output, expected_output)

    def test_update_non_existent_class(self):
        """
        Checks error management for update command: Class name not found
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update NonexistentClass")
            output = f.getvalue()
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(output, expected_output)

    def test_update_instance_id_missing(self):
        """
        Checks error management for update command: No id entered
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            output = f.getvalue()
            expected_output = "** instance id missing **\n"
            self.assertEqual(output, expected_output)

    def test_update_no_instance_found(self):
        """
        Check error management for update command: no match of instance with id
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 57584939")
            output = f.getvalue()
            expected_output = "** no instance found **\n"
            self.assertEqual(output, expected_output)

    def test_precmd(self):
        """checks that the format of the line set by 'precmd' is as expected
        """
        inst = City()
        ln = HBNBCommand().precmd(f'City.update("{inst.id}", "name", "Offal")')
        self.assertEqual(ln, f'update City {inst.id} "name" "Offal"')
