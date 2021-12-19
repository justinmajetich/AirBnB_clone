#!/usr/bin/python3
"""
Test Console
"""
import pycodestyle
# import pep8
import unittest
import inspect
from unittest.mock import patch
from unittest.mock import MagicMock
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import json
from io import StringIO
import os


class TestCodeFormat(unittest.TestCase):
    """
    A class to test pep8 on base_model file"""
    # def test_pep8(self):
    #     """
    #     Test pep8 format
    #     """
    #     pep8style = pep8.StyleGuide(quiet=True)
    #     result = pep8style.check_files(['console.py'])
    #     self.assertEqual(result.total_errors, 0,
    #                      "Found code style errors (and warnings).")

    def test_pycodestyle(self):
        """
        Test pep8 format
        """
        pycostyle = pycodestyle.StyleGuide(quiet=True)
        result = pycostyle.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class Test_docstrings(unittest.TestCase):
    """Test docstrings"""
    @classmethod
    def setup_class(self):
        """
        inspect.getmembers(object, [predicate])
        Return all the members of an object in a list of (name, value)
        pairs sorted by name
        only members for which the predicate returns a true value are included
        """
        self.obj_members(HBNBCommand, inspect.isfunction)
        self.console = HBNBCommand()

    def test_module_dostring(self):
        """
        Test for exist module docstrings
        """
        self.assertIsNotNone(console.__doc__,
                             "console.py file needs a docstrings")
        self.assertTrue(len(__doc__) > 0, "console.py have docstrings")
        self.assertTrue(len(__doc__) > 0, " console don't have docstrings")
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_help.__doc__)
        self.assertIsNotNone(HBNBCommand.help_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.help_quit.__doc__)

    def test_invalid_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Luffy")
            self.assertEqual('*** Unknown syntax: Luffy\n' or '', f.getvalue())

    def test_empty_line(self):
        """Testing empty input"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """Testing quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual('', f.getvalue())


class Test_Help(unittest.TestCase):
    """Testing help command"""

    @classmethod
    def setup_class(self):
        """setting class up"""
        self.console = HBNBCommand()

    def help_command(self):
        """Testing an only help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = '\nDocumented commands (type help <topic>[103 chars]\n\n)'
            self.assertEqual(output, f.getvalue())

    def help_help_command(self):
        """Test comand help EOF"""
        expected = 'End of File command: exit the program\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(expected, f.getvalue())

    def all_help_command(self):
        """test commands: help all"""
        expected = 'Prints all string representation of all instances \
            based or not on the class name \
            Ex: $ all BaseModel or $ all.\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(expected, f.getvalue())

    def create_help_command(self):
        """test commands: help create"""
        expected = 'Creates a new instance of BaseModel, saves it \n \
            (to the JSON file) and prints the id\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(expected, f.getvalue())

    def quit_help_command(self):
        """test commands: help quit"""
        expected = 'Quit command to exit the program\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(expected, f.getvalue())

    def destroy_help_command(self):
        """test commands: help destroy"""
        expected = 'Deletes an instance based on the class name and\n \
        id (save the change into the JSON file).\n \
        Ex: $ destroy BaseModel 1234-1234-1234\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(expected, f.getvalue())

    def show_help_command(self):
        """test commands: help show"""
        expected = 'Prints the string representation of an instance\n \
            based on the class name and id.\n \
            Ex: $ show BaseModel 1234-1234-1234.'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(expected, f.getvalue())

    def update_help_command(self):
        """test commands: help update"""
        expected = 'Updates an instance based on the class name and id\n \
            by adding or updating attribute\n \
            (save the change into the JSON file).\n \
            - Usage:\n \
            update <class name> <id> <attribute name> "<attribute value>"\n \
            - Ex:\n \
            $ update BaseModel 1234-1234-1234 email\
                 "aibnb@holbertonschool.com"\n \
            - Only one attribute can be updated at the time\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(expected, f.getvalue())


class CreateTest(unittest.TestCase):
    """testing command test in console"""

    @classmethod
    def setUpClass(self):
        """setting class up"""
        self.console = HBNBCommand()

    def test_create(self):
        """testing creat input"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create holbieees")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertEqual(
                            '["[User', f.getvalue()[:7])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        self.assertRegex(f.getvalue(), '^[0-9a-f]{8}-[0-9a-f]{4}-[1-5]'
                                       '[0-9a-f]{3}-[89ab][0-9a-f]{3}-'
                                       '[0-9a-f]{12}$')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        self.assertRegex(f.getvalue(), '^[0-9a-f]{8}-[0-9a-f]{4}-[1-5]'
                                       '[0-9a-f]{3}-[89ab][0-9a-f]{3}-'
                                       '[0-9a-f]{12}$')


class ShowTest(unittest.TestCase):
    """testing command show in console"""

    @classmethod
    def setUpClass(self):
        """setting class up"""
        self.console = HBNBCommand()

    def test_show(self):
        """testing show's behaviour"""
        try:
            os.remove("file.json")
        except Exception as f:
            pass

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show holbieees")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual("** instance id missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show" + "User " + id)
        self.assertIsNotNone(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show" + "User " + id)
        self.assertIsNotNone(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show(1)")
            expected = "*** Unknown syntax: User.show(1)\n"
        self.assertEqual(f.getvalue(), expected)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("sdasdasd.show(1)")
            expected = "*** Unknown syntax: sdasdasd.show(1)\n"
        self.assertEqual(f.getvalue(), expected)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show()")
            expected = "*** Unknown syntax: User.show()\n"
        self.assertEqual(f.getvalue(), expected)

    def test_count(self):
        """Validate count method"""
        try:
            os.remove("file.json")
        except Exception as f:
            pass

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
        self.assertNotEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("id.count()")
            expectect = "*** Unknown syntax: id.count()\n"
        self.assertEqual(f.getvalue(), expectect)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count(d)")
        self.assertEqual(f.getvalue(), '*** Unknown syntax: User.count(d)\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()d")
        self.assertEqual(f.getvalue(), '*** Unknown syntax: User.count()d\n')

    def test_destroy(self):
        """testing destroy's behaviour"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy holbies")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual("** instance id missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 123123")
            self.assertEqual("** no instance found **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy(1)")
            expectet = "*** Unknown syntax: User.destroy(1)\n"
        self.assertEqual(f.getvalue(), expectet)

    def test_all(self):
        """Validate show in both ways"""
        try:
            os.remove("file.json")
        except Exception as f:
            pass
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        self.assertNotEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        self.assertNotEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all 123123")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all State")
            self.assertEqual('["[Stat', f.getvalue()[:7])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("ssss.all()")
        self.assertEqual(f.getvalue(), '*** Unknown syntax: ssss.all()\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all(dasds)")
        self.assertEqual(f.getvalue(), '*** Unknown syntax: User.all(dasds)\n')

    def test_update(self):
        """Validate all both ways"""
        try:
            os.remove("file.json")
        except Exception as f:
            pass
        """Testing update's behaviour"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        id = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update holbies")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 123123")
            self.assertEqual("** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            obj = f.getvalue()
        my_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + my_id)
            self.assertEqual("** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + my_id + " Name")
            self.assertEqual(
                "** value missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + id + " name " + "Goku")
        self.assertNotEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            expectect = "*** Unknown syntax: asdasd.update()\n"
            HBNBCommand().onecmd("asdasd.update()")
        self.assertEqual(f.getvalue(), expectect)
        with patch('sys.stdout', new=StringIO()) as f:
            expectect = "*** Unknown syntax: User.update()\n"
            HBNBCommand().onecmd("User.update()")
        self.assertEqual(f.getvalue(), expectect)


if __name__ == '__main__':
    unittest.main()
