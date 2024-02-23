#!/usr/bin/python3
"""
Unittest for the console including the class HBNBCommand
"""

import unittest
import models
from models.user import User
import os
import pep8
import inspect
import json
import time
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from unittest.mock import patch


class TestConsoleDocumentationAndStyle(unittest.TestCase):
    """
    Tests for the HBNBCommand class documentation and style.
    """

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.console_funcs = inspect.getmembers(
                HBNBCommand, predicate=inspect.isfunction
                )

    def test_pep8_conformance_Console(self):
        """
        Test that console.py conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["console.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_console(self):
        """
        Test that tests/test_console.py conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_console.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_console_class_docstring(self):
        """
        Test for the HBNBCommand class docstring
        """
        self.assertIsNot(
                HBNBCommand.__doc__,
                None,
                "HBNBCommand class needs a docstring"
                )
        self.assertTrue(
            len(HBNBCommand.__doc__) >= 1,
            "HBNBCommand class needs a docstring"
        )


class TestConsole_Base(unittest.TestCase):
    """This class defines unittests for the basic usage of the console"""

    def test_docstr(self):
        """Test class documentaion"""
        self.assertTrue(len(HBNBCommand.__doc__) > 2)

    def test_prompt(self):
        """This function tests having the correct prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_quit_return(self):
        """This function tests the return of onecmd function during quitting"""
        # with patch('sys.stdout', new=StringIO()) as f:
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_eof_return(self):
        """This function tests the return of onecmd function during eof"""
        # with patch('sys.stdout', new=StringIO()) as f:
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_invalid_cmd(self):
        """This function tests the output when the class recieves
        invalid cmd"""
        invalid_output = "*** Unknown syntax: arg"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("arg"))
            self.assertEqual(invalid_output, f.getvalue().strip())

    def test_empty_line(self):
        """This function tests recieving an empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())

    def test_help(self):
        """This function tests the expected output of the command help"""
        cmds = ['EOF', 'all', 'count', 'create', 'destroy',
                'help', 'quit', 'show', 'update']
        expected = ("Documented commands (type help <topic>):\n",
                    "========================================\n",
                    '  '.join(cmds))
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(''.join(expected), f.getvalue().strip())


class TestConsole_help(unittest.TestCase):
    """This class defines unittests for the help method of the console"""

    def test_help_EOF(self):
        """This function tests the <help EOF> message content"""
        expected = "Exits the program without formatting"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(expected, f.getvalue().strip())

    def test_help_all(self):
        """This function tests the <help all> message content"""
        out = ["Shows all objects, or all of a class\n",
               "[Usage]: all <className>"]
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual("".join(out), f.getvalue().strip())

    def test_help_count(self):
        """This function tests the <help count> message content"""
        out = "Usage: count <class_name>"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(out, f.getvalue().strip())

    def test_help_create(self):
        """This function tests the <help create> message content"""
        out = ["Creates a new instance of the class provided, save it into\n",
               "        a JSON file, and prints the id"]
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(''.join(out), f.getvalue().strip())

    def test_help_destroy(self):
        """This function tests the <help destroy> message content"""
        out = ["Destroys an individual instance of a class\n",
               "[Usage]: destroy <className> <objectId>"]
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual("".join(out), f.getvalue().strip())

    def test_help_help(self):
        """This function tests the <help help> message content"""
        out = ['List available commands with "help" or detailed',
               'help with "help cmd".']
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help help"))
            self.assertEqual(" ".join(out), f.getvalue().strip())

    def test_help_quit(self):
        """This function tests the <help quit> message content"""
        out = "Exits the program with formatting"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(out, f.getvalue().strip())

    def test_help_show(self):
        """This function tests the <help show> message content"""
        out = ["Shows an individual instance of a class\n",
               "[Usage]: show <className> <objectId>"]
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(''.join(out), f.getvalue().strip())

    def test_help_create(self):
        """This function tests the <help update> message content"""
        o = ["Updates an object with new information\n",
             "Usage: update <className> <id> <attName> <attVal>"]
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual("".join(o), f.getvalue().strip())


class TestConsole_create(unittest.TestCase):
    """This class defines unittests for the create method of the console"""

    @classmethod
    def setUpClass(cls):
        """sets up the environment for testing"""
        if os.getenv("HBNB_TYPE_STORAGE") != "db":
            try:
                os.remove("file.json")
            except IOError:
                pass
            models.storage._FileStorage__objects = {}
        else:
            pass

    def tearDown(self):
        """removes files created and resets the value of __objects"""
        if os.getenv("HBNB_TYPE_STORAGE") != "db":
            try:
                os.remove("file.json")
            except IOError:
                pass
            models.storage._FileStorage__objects = {}
        else:
            pass

    def test_create_invalid(self):
        """This function tests create command with missing class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual("** class name missing **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Model"))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_create_invalid_method(self):
        """This function tests create command with missing arguments
        in method format"""
        out1 = "*** Unknown syntax: Model.create()"
        out2 = "*** Unknown syntax: User.create()"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Model.create()"))
            self.assertEqual(out1, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.create()"))
            self.assertEqual(out2, f.getvalue().strip())

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') == 'db',
            "skip if storage type is db")
    def test_create_cmd_basemodel(self):
        """This method creates a new BaseModel"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        with open(models.storage._FileStorage__file_path,
                  encoding="utf-8") as file:
            read_data = file.read()
            self.assertIn("BaseModel." + obj_id, read_data)
        self.assertIn("BaseModel." + obj_id, models.storage.all().keys())

    def test_create_cmd_user(self):
        """This method creates a new User"""
        from models.user import User
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create User'))
                self.assertEqual("** email missing **", f.getvalue().strip())
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create User'))
                obj_id = f.getvalue().strip()
            with open(
                    models.storage._FileStorage__file_path, encoding="utf-8"
                    ) as file:
                read_data = file.read()
                self.assertIn("User." + obj_id, read_data)
            self.assertIn("User." + obj_id, models.storage.all().keys())

    def test_create_cmd_city(self):
        """this method creates a new city"""
        from models.city import City
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create City'))
                self.assertEqual(
                        "** state_id missing **", f.getvalue().strip()
                        )
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create City'))
                obj_id = f.getvalue().strip()
            with open(
                    models.storage._FileStorage__file_path, encoding="utf-8"
                    ) as file:
                read_data = file.read()
                self.assertIn("City." + obj_id, read_data)
            self.assertIn("City." + obj_id, models.storage.all().keys())

    def test_create_cmd_state(self):
        """this method creates a new state"""
        from models.state import State
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create State'))
                self.assertEqual("** name missing **", f.getvalue().strip())
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create State'))
                obj_id = f.getvalue().strip()
            with open(
                    models.storage._FileStorage__file_path, encoding="utf-8"
                    ) as file:
                read_data = file.read()
                self.assertIn("State." + obj_id, read_data)
            self.assertIn("State." + obj_id, models.storage.all().keys())

    def test_create_cmd_amenity(self):
        """this method creates a new amenity"""
        from models.state import State
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create Amenity'))
                self.assertEqual("** name missing **", f.getvalue().strip())
        else:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd("create Amenity"))
                obj_id = f.getvalue().strip()
            with open(
                    models.storage._FileStorage__file_path,
                    encoding="utf-8"
                    ) as file:
                read_data = file.read()
                self.assertIn("Amenity." + obj_id, read_data)
            self.assertIn("Amenity." + obj_id, models.storage.all().keys())

    def test_create_user(self):
        """Test create command for User"""
        from models.user import User
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(
                    'create User email="test@test.com" password="123test"'
                    ))
                obj_id = f.getvalue().strip().strip().split('\n')[-1]
            models.storage.reload()
            obj = models.storage.all()["User." + obj_id]
            self.assertEqual(getattr(obj, "email"), "test@test.com")
            self.assertEqual(getattr(obj, "password"), "123test")
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(
                    HBNBCommand().onecmd(
                        'create User email="test@test.com" password="test" '
                        'first_name="John" last_name="Doe"'
                    )
                )
                obj_id = f.getvalue().strip()
            obj = models.storage.all()["User." + obj_id]
            self.assertEqual(getattr(obj, "email"), "test@test.com")
            self.assertEqual(getattr(obj, "password"), "test")
            self.assertEqual(getattr(obj, "first_name"), "John")
            self.assertEqual(getattr(obj, "last_name"), "Doe")

    def test_create_city(self):
        """Test create command for City"""
        from models.city import City
        from models.state import State
        # Create a State with a name
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(
                HBNBCommand().onecmd(
                    'create State name="Khartoum"'
                )
            )
            state_id = f.getvalue().strip().split('\n')[-1]
        state = models.storage.all()["State." + state_id]
        self.assertEqual(getattr(state, "name"), "Khartoum")

        # Now create the City with the generated state_id
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(
                HBNBCommand().onecmd(
                    f'create City name="test" state_id="{state_id}"'
                )
            )
            city_id = f.getvalue().strip()
        models.storage.reload()
        city = models.storage.all()["City." + city_id]
        self.assertEqual(getattr(city, "name"), "test")
        self.assertEqual(getattr(city, "state_id"), state_id)

    def test_create_state(self):
        """Test create command for State"""
        from models.state import State
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(
                        HBNBCommand().onecmd('create State name="test"')
                        )
                obj_id = f.getvalue().strip().strip().split('\n')[-1]
            models.storage.reload()
            obj = models.storage.all()["State." + obj_id]
            self.assertEqual(getattr(obj, "name"), "test")
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(
                        HBNBCommand().onecmd('create State name="test"')
                        )
                obj_id = f.getvalue().strip()
            obj = models.storage.all()["State." + obj_id]
            self.assertEqual(getattr(obj, "name"), "test")

    def test_create_cmd_amenity(self):
        """this method creates a new amenity"""
        from models.amenity import Amenity
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create Amenity'))
                self.assertEqual("** name missing **", f.getvalue().strip())
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd("create Amenity"))
                obj_id = f.getvalue().strip()
            obj = models.storage.all()["Amenity." + obj_id]
            self.assertTrue(isinstance(obj, Amenity))

    def test_create_place(self):
        """Test create command for Place"""
        from models.place import Place
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(
                    'create Place '
                    'name="test" description="test" number_rooms=2 '
                    'number_bathrooms=1 max_guest=3 price_by_night=100 '
                    'latitude=10.0 longitude=10.0 amenity_ids=["test"]'
                    ))
                self.assertEqual("** city_id missing **", f.getvalue().strip())
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(
                    HBNBCommand().onecmd(
                        'create Place city_id="test" user_id="test" '
                        'name="test" description="test" number_rooms=2 '
                        'number_bathrooms=1 max_guest=3 price_by_night=100 '
                        'latitude=10.0 longitude=10.0 amenity_ids=["test"]'
                    )
                )
                obj_id = f.getvalue().strip()
            obj = models.storage.all()["Place." + obj_id]
            self.assertEqual(getattr(obj, "city_id"), "test")
            self.assertEqual(getattr(obj, "user_id"), "test")
            self.assertEqual(getattr(obj, "name"), "test")
            self.assertEqual(getattr(obj, "description"), "test")
            self.assertEqual(getattr(obj, "number_rooms"), 2)
            self.assertEqual(getattr(obj, "number_bathrooms"), 1)
            self.assertEqual(getattr(obj, "max_guest"), 3)
            self.assertEqual(getattr(obj, "price_by_night"), 100)
            self.assertEqual(getattr(obj, "latitude"), 10.0)
            self.assertEqual(getattr(obj, "longitude"), 10.0)
            self.assertEqual(getattr(obj, "amenity_ids"), ["test"])

    def test_create_review_db(self):
        """Test create command for Review when HBNB_TYPE_STORAGE=db"""
        from models.review import Review
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.state import State

        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Create a State
            with patch("sys.stdout", new=StringIO()) as f:
                HBNBCommand().onecmd('create State name="test_state"')
                state_id = f.getvalue().strip()
            models.storage.reload()
            state = models.storage.all().get("State." + state_id)
            self.assertIsNotNone(state, "State not found in storage")
            self.assertEqual(getattr(state, "name"), "test state")

            # Create a City with the generated state_id
            with patch("sys.stdout", new=StringIO()) as f:
                HBNBCommand().onecmd(
                        f'create City name="test_city" state_id="{state_id}"'
                        )
                city_id = f.getvalue().strip()
            models.storage.reload()
            city = models.storage.all().get("City." + city_id)
            self.assertIsNotNone(city, "City not found in storage")
            self.assertEqual(getattr(city, "name"), "test city")

            # Create a User
            with patch("sys.stdout", new=StringIO()) as f:
                HBNBCommand().onecmd(
                        'create User email="user@test.com" password="pwd"'
                        )
                user_id = f.getvalue().strip()
            models.storage.reload()
            user = models.storage.all().get("User." + user_id)
            self.assertIsNotNone(user, "User not found in storage")
            self.assertEqual(getattr(user, "email"), "user@test.com")

            # Create a Place with the generated city_id and user_id
            with patch("sys.stdout", new=StringIO()) as f:
                HBNBCommand().onecmd(
                        f'create Place user_id="{user_id}" '
                        f'name="test_place" city_id="{city_id}"'
                        )
                place_id = f.getvalue().strip()
            models.storage.reload()
            place = models.storage.all().get("Place." + place_id)
            self.assertIsNotNone(place, "Place not found in storage")
            self.assertEqual(getattr(place, "name"), "test place")

            # Now create the Review with the generated user_id and place_id
            with patch("sys.stdout", new=StringIO()) as f:
                HBNBCommand().onecmd(
                        f'create Review text="test_review" '
                        f'user_id="{user_id}" place_id="{place_id}"'
                        )
                review_id = f.getvalue().strip()
            models.storage.reload()
            review = models.storage.all().get("Review." + review_id)
            self.assertIsNotNone(review, "Review not found in storage")
            self.assertEqual(getattr(review, "text"), "test review")
            self.assertEqual(getattr(review, "user_id"), user_id)
            self.assertEqual(getattr(review, "place_id"), place_id)

    def test_create_user_with_invalid_parameters(self):
        """Test create command for User with invalid parameters"""
        from models.user import User
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(
                        HBNBCommand().onecmd('create User invalid="invalid"')
                        )
                self.assertEqual("** email missing **", f.getvalue().strip())
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(
                    HBNBCommand().onecmd('create User invalid="invalid"')
                )
                obj_id = f.getvalue().strip()
            obj = models.storage.all()["User." + obj_id]
            self.assertFalse(hasattr(obj, "invalid"))

    def test_create_city_with_invalid_parameters(self):
        """Test create command for City with invalid parameters"""
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(
                        HBNBCommand().onecmd('create City invalid="invalid"')
                        )
                self.assertEqual(
                        "** state_id missing **",
                        f.getvalue().strip()
                        )
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(
                        HBNBCommand().onecmd('create City invalid="invalid"')
                        )
                obj_id = f.getvalue().strip()
            obj = models.storage.all()["City." + obj_id]
            self.assertFalse(hasattr(obj, "invalid"))

    def test_create_state_with_invalid_parameters(self):
        """Test create command for State with invalid parameters"""
        from models.state import State
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(
                        HBNBCommand().onecmd('create State invalid="invalid"')
                        )
                self.assertEqual("** name missing **", f.getvalue().strip())
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(
                    HBNBCommand().onecmd('create State invalid="invalid"')
                )
                obj_id = f.getvalue().strip()
            obj = models.storage.all()["State." + obj_id]
            self.assertFalse(hasattr(obj, "invalid"))

    def test_create_amenity_with_invalid_parameters(self):
        """Test create command for Amenity with invalid parameters"""
        from models.amenity import Amenity
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(
                        HBNBCommand().onecmd(
                            'create Amenity invalid="invalid"'
                            )
                        )
                self.assertEqual("** name missing **", f.getvalue().strip())
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(
                    HBNBCommand().onecmd('create Amenity invalid="invalid"')
                )
                obj_id = f.getvalue().strip()
            obj = models.storage.all()["Amenity." + obj_id]
            self.assertFalse(hasattr(obj, "invalid"))

    def test_create_place_with_invalid_parameters(self):
        """Test create command for Place with invalid parameters"""
        from models.place import Place
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(
                        HBNBCommand().onecmd('create Place invalid="invalid"')
                        )
                self.assertEqual("** city_id missing **", f.getvalue().strip())
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(
                    HBNBCommand().onecmd('create Place invalid="invalid"')
                )
                obj_id = f.getvalue().strip()
            obj = models.storage.all()["Place." + obj_id]
            self.assertFalse(hasattr(obj, "invalid"))

    def test_create_review_with_invalid_parameters(self):
        """Test create command for Review with invalid parameters"""
        from models.review import Review
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(
                        HBNBCommand().onecmd('create Review invalid="invalid"')
                        )
                self.assertEqual(
                        "** place_id missing **",
                        f.getvalue().strip()
                        )
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(
                    HBNBCommand().onecmd('create Review invalid="invalid"')
                )
                obj_id = f.getvalue().strip()
            obj = models.storage.all()["Review." + obj_id]
            self.assertFalse(hasattr(obj, "invalid"))

    def test_create_user_with_no_parameters(self):
        """Test create command for User with no parameters"""
        from models.user import User
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create User'))
                self.assertEqual("** email missing **", f.getvalue().strip())
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create User'))
                obj_id = f.getvalue().strip()
            obj = models.storage.all()["User." + obj_id]
            self.assertTrue(isinstance(obj, User))

    def test_create_city_with_no_parameters(self):
        """Test create command for City with no parameters"""
        from models.city import City
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create City'))
                self.assertEqual(
                        "** state_id missing **",
                        f.getvalue().strip()
                        )
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create City'))
                obj_id = f.getvalue().strip()
            obj = models.storage.all()["City." + obj_id]
            self.assertTrue(isinstance(obj, City))

    def test_create_state_with_no_parameters(self):
        """Test create command for State with no parameters"""
        from models.state import State
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create State'))
                self.assertEqual("** name missing **", f.getvalue().strip())
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create State'))
                obj_id = f.getvalue().strip()
            obj = models.storage.all()["State." + obj_id]
            self.assertTrue(isinstance(obj, State))

    def test_create_amenity_with_no_parameters(self):
        """Test create command for Amenity with no parameters"""
        from models.amenity import Amenity
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create Amenity'))
                self.assertEqual("** name missing **", f.getvalue().strip())
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create Amenity'))
                obj_id = f.getvalue().strip()
            obj = models.storage.all()["Amenity." + obj_id]
            self.assertTrue(isinstance(obj, Amenity))

    def test_create_place_with_no_parameters(self):
        """Test create command for Place with no parameters"""
        from models.place import Place
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create Place'))
                self.assertEqual("** city_id missing **", f.getvalue().strip())
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create Place'))
                obj_id = f.getvalue().strip()
            obj = models.storage.all()["Place." + obj_id]
            self.assertTrue(isinstance(obj, Place))

    def test_create_review_with_no_parameters(self):
        """Test create command for Review with no parameters"""
        from models.review import Review
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            # Behavior when HBNB_TYPE_STORAGE=db
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create Review'))
                self.assertEqual(
                        "** place_id missing **",
                        f.getvalue().strip()
                        )
        else:
            with patch("sys.stdout", new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create Review'))
                obj_id = f.getvalue().strip()
            obj = models.storage.all()["Review." + obj_id]
            self.assertTrue(isinstance(obj, Review))

    def test_create_with_nonexistent_class(self):
        """Test create command with nonexistent class"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('create NonexistentClass'))
        self.assertEqual("** class doesn't exist **", f.getvalue().strip())


class TestConsole_show(unittest.TestCase):
    """This class defines unittests for the create method of the console"""

    @classmethod
    def setUpClass(cls):
        """sets up the environment for testing"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        models.storage._FileStorage__objects = {}

    def tearDown(self):
        """removes files created and resets the value of __objects"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        models.storage._FileStorage__objects = {}

    def test_show_invalid(self):
        """This function tests show command with missing class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual("** class name missing **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Model"))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Model.show()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_show_instance_id_missing(self):
        """This function tests every possibility of recieving "id missing"
        msg"""
        msg = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show State"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show City"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Amenity"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Place"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Review"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("BaseModel.show()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("User.show()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("State.show()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("City.show()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Amenity.show()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Place.show()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Review.show()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') == 'db',
            "skip if storage type is db"
            )
    def test_show_invalid_id(self):
        """This function tests all the possibilities of recieving an
        invalid id msg"""
        msg = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show State 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show City 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Place 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Amenity 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Review 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd('BaseModel.show("1212121")')
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd('User.show("1212121")')
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("State.show('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("City.show('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Place.show('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Amenity.show('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Review.show('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') == 'db',
            "skip if storage type is db"
            )
    def test_show_objs(self):
        """This function tests the functionality of the show method"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel " + obj_id))
            obj = models.storage.all()["BaseModel." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User " + obj_id))
            obj = models.storage.all()["User." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show State " + obj_id))
            obj = models.storage.all()["State." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show City " + obj_id))
            obj = models.storage.all()["City." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Amenity " + obj_id))
            obj = models.storage.all()["Amenity." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Place " + obj_id))
            obj = models.storage.all()["Place." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show Review " + obj_id))
            obj = models.storage.all()["Review." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel " + obj_id))
            obj = models.storage.all()["BaseModel." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') == 'db',
            "skip if storage type is db"
            )
    def test_show_method_format(self):
        """This function tests the show method in the dot notation"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("BaseModel.show('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            obj = models.storage.all()["BaseModel." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("User.show('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            obj = models.storage.all()["User." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("State.show('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            obj = models.storage.all()["State." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("City.show('{}') ".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            obj = models.storage.all()["City." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Amenity.show('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            obj = models.storage.all()["Amenity." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Place.show('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            obj = models.storage.all()["Place." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Review.show('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            obj = models.storage.all()["Review." + obj_id]
            self.assertEqual(f.getvalue().strip(), str(obj))


class TestConsole_destroy(unittest.TestCase):
    """This class defines unittests for the destroy method of the console"""

    @classmethod
    def setUpClass(cls):
        """sets up the environement for testing"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        models.storage._FileStorage__objects = {}

    def tearDown(self):
        """removes files created and resets the value of __objects"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        models.storage._FileStorage__objects = {}

    def test_destroy_invalid(self):
        """This function tests destroy command with missing class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual("** class name missing **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Model"))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Model.destroy()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_destroy_instance_id_missing(self):
        """This function tests every possibility of recieving
        "id missing" msg"""
        msg = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("BaseModel.destroy()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("User.destroy()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("State.destroy()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("City.destroy()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Amenity.destroy()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Place.destroy()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Review.destroy()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())

    def test_destroy_invalid_id(self):
        """This function tests all the possibilities of recieving an
        invalid id msg"""
        msg = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy State 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy City 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Place 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Review 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd('BaseModel.destroy("1212121")')
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd('User.destroy("1212121")')
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("State.destroy('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("City.destroy('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Place.destroy('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Amenity.destroy('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Review.destroy('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') == 'db',
            "skip if storage type is db"
            )
    def test_destroy_objs(self):
        """This function tests the functionality of the destroy method"""
        msg = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel " + _id))
            self.assertNotIn("BaseModel." + _id, models.storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User " + obj_id))
            self.assertNotIn("User." + obj_id, models.storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy State " + obj_id))
            self.assertNotIn("State." + obj_id, models.storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy City " + obj_id))
            self.assertNotIn("City." + obj_id, models.storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity " + obj_id))
            self.assertNotIn("Amenity." + obj_id, models.storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Place " + obj_id))
            self.assertNotIn("Place." + obj_id, models.storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Review " + obj_id))
            self.assertNotIn("Place." + obj_id, models.storage.all())

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') == 'db',
            "skip if storage type is db"
            )
    def test_destroy_method_format(self):
        """This function tests the destroy method in the dot notation"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            li = HBNBCommand().precmd("BaseModel.destroy('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(li))
            self.assertNotIn("BaseModel." + obj_id, models.storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("User.destroy('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertNotIn("User." + obj_id, models.storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("State.destroy('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertNotIn("State." + obj_id, models.storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("City.destroy('{}') ".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertNotIn("City." + obj_id, models.storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Amenity.destroy('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertNotIn("Amenity." + obj_id, models.storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Place.destroy('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertNotIn("Place." + obj_id, models.storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Review.destroy('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertNotIn("Review." + obj_id, models.storage.all())


@unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "skip if storage type is db"
        )
class TestConsole_all(unittest.TestCase):
    """This class defines unittests for the all method of the console"""

    @classmethod
    def setUpClass(cls):
        """sets up the environment for testing"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        models.storage._FileStorage__objects = {}

    def tearDown(self):
        """removes files created and resets the value of __objects"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        models.storage._FileStorage__objects = {}

    def test_all_invalid(self):
        """This function tests all command with missing class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all Model"))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Model.all()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_all_objs(self):
        """This function tests the functionality of the all method"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("User", f.getvalue().strip())
            self.assertIn("State", f.getvalue().strip())
            self.assertIn("City", f.getvalue().strip())
            self.assertIn("Amenity", f.getvalue().strip())
            self.assertIn("Place", f.getvalue().strip())
            self.assertIn("Review", f.getvalue().strip())

    def test_all_cls(self):
        """This function tests the functionality of all with arg method"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn("User", f.getvalue().strip())
            list_obj = json.loads(f.getvalue().strip())
            self.assertIs(type(list_obj), list)
            self.assertTrue(all("User" in d_ for d_ in list_obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn("State", f.getvalue().strip())
            list_obj = json.loads(f.getvalue().strip())
            self.assertIs(type(list_obj), list)
            self.assertTrue(all("State" in d_ for d_ in list_obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn("City", f.getvalue().strip())
            list_obj = json.loads(f.getvalue().strip())
            self.assertIs(type(list_obj), list)
            self.assertTrue(all("City" in d_ for d_ in list_obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn("Amenity", f.getvalue().strip())
            list_obj = json.loads(f.getvalue().strip())
            self.assertIs(type(list_obj), list)
            self.assertTrue(all("Amenity" in d_ for d_ in list_obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn("Place", f.getvalue().strip())
            list_obj = json.loads(f.getvalue().strip())
            self.assertIs(type(list_obj), list)
            self.assertTrue(all("Place" in d_ for d_ in list_obj))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn("Review", f.getvalue().strip())
            list_obj = json.loads(f.getvalue().strip())
            self.assertIs(type(list_obj), list)
            self.assertTrue(all("Review" in d_ for d_ in list_obj))

    def test_all_cls_method(self):
        """This function tests the functionality of all with arg method"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("User.all()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertIn("User", f.getvalue().strip())
            list_obj = json.loads(f.getvalue().strip())
            self.assertIs(type(list_obj), list)
            self.assertTrue(all("User" in d_ for d_ in list_obj))
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("State.all()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertIn("State", f.getvalue().strip())
            list_obj = json.loads(f.getvalue().strip())
            self.assertIs(type(list_obj), list)
            self.assertTrue(all("State" in d_ for d_ in list_obj))
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("City.all()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertIn("City", f.getvalue().strip())
            list_obj = json.loads(f.getvalue().strip())
            self.assertIs(type(list_obj), list)
            self.assertTrue(all("City" in d_ for d_ in list_obj))
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Amenity.all()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertIn("Amenity", f.getvalue().strip())
            list_obj = json.loads(f.getvalue().strip())
            self.assertIs(type(list_obj), list)
            self.assertTrue(all("Amenity" in d_ for d_ in list_obj))
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Place.all()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertIn("Place", f.getvalue().strip())
            list_obj = json.loads(f.getvalue().strip())
            self.assertIs(type(list_obj), list)
            self.assertTrue(all("Place" in d_ for d_ in list_obj))
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Review.all()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertIn("Review", f.getvalue().strip())
            list_obj = json.loads(f.getvalue().strip())
            self.assertIs(type(list_obj), list)
            self.assertTrue(all("Review" in d_ for d_ in list_obj))


@unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "skip if storage type is db"
        )
class TestConsole_update(unittest.TestCase):
    """This class defines unittests for the update method of the console"""

    @classmethod
    def setUpClass(cls):
        '''Remove the file/db at the beginning of the test'''
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            os.environ['HBNB_ENV'] = 'test'
        else:
            try:
                models.FileStorage._FileStorage__objects = {}
                os.remove(models.FileStorage._FileStorage__file_path)
            except FileNotFoundError:
                pass

    def tearDown(self):
        """removes files created and resets the value of __objects"""
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            os.environ['HBNB_ENV'] = 'test'
        else:
            try:
                os.remove("file.json")
            except IOError:
                pass
            models.storage._FileStorage__objects = {}

    def test_update_invalid(self):
        """This function tests update command with missing class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual("** class name missing **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update Model"))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Model.update()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_update_instance_id_missing(self):
        """This function tests every possibility of recieving
        "id missing" msg"""
        msg = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update State"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update City"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update Amenity"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update Place"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update Review"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("BaseModel.update()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("User.update()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("State.update()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("City.update()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Amenity.update()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Place.update()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Review.update()")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())

    def test_update_invalid_id(self):
        """This function tests all the possibilities of recieving an
        invalid id msg"""
        msg = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update User 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update State 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update City 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update Place 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update Amenity 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update Review 1212121"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd('BaseModel.update("1212121")')
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd('User.update("1212121")')
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("State.update('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("City.update('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Place.update('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Amenity.update('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Review.update('1212121')")
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_update_missing_name(self):
        """This function tests the functionality of the update method"""
        msg = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel " + _id))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update User " + obj_id))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update State " + obj_id))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update City " + obj_id))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update Amenity " + obj_id))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update Place " + obj_id))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update Review " + obj_id))
            self.assertEqual(msg, f.getvalue().strip())

    def test_update_missing_name_method(self):
        """This function tests the update method in the dot notation"""
        msg = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            li = HBNBCommand().precmd("BaseModel.update('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(li))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("User.update('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("State.update('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("City.update('{}') ".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Amenity.update('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Place.update('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            line = HBNBCommand().precmd("Review.update('{}')".format(obj_id))
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())

    def test_update_missing_value(self):
        """This function tests the functionality of the update method"""
        msg = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "update BaseModel " + _id + " value"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "update User " + obj_id + " value"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "update State " + obj_id + " value"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "update City " + obj_id + " value"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "update Amenity " + obj_id + " value"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "update Place " + obj_id + " value"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "update Review " + obj_id + " value"
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(msg, f.getvalue().strip())

    def test_update_missing_value_method(self):
        """This function tests the update method in the dot notation"""
        msg = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "BaseModel.update('{}' name)".format(obj_id)
            li = HBNBCommand().precmd(cmd)
            self.assertFalse(HBNBCommand().onecmd(li))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "User.update('{}', 'name')".format(obj_id)
            line = HBNBCommand().precmd(cmd)
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "State.update('{}', 'name')".format(obj_id)
            line = HBNBCommand().precmd(cmd)
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "City.update('{}', 'name')".format(obj_id)
            line = HBNBCommand().precmd(cmd)
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "Amenity.update('{}', 'name')".format(obj_id)
            line = HBNBCommand().precmd(cmd)
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "Place.update('{}', 'name')".format(obj_id)
            line = HBNBCommand().precmd(cmd)
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "Review.update('{}', 'name')".format(obj_id)
            line = HBNBCommand().precmd(cmd)
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(msg, f.getvalue().strip())

    def test_update_objs(self):
        """This function tests the functionality of the update method"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = f.getvalue().strip()
        cmd = "update BaseModel " + _id + " name" + " value"
        self.assertFalse(HBNBCommand().onecmd(cmd))
        attr = models.storage.all()["BaseModel." + _id].__dict__
        self.assertIn("name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = f.getvalue().strip()
        cmd = "update User " + _id + " name" + " value"
        self.assertFalse(HBNBCommand().onecmd(cmd))
        attr = models.storage.all()["User." + _id].__dict__
        self.assertIn("name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            _id = f.getvalue().strip()
        cmd = "update State " + _id + " name" + " value"
        self.assertFalse(HBNBCommand().onecmd(cmd))
        attr = models.storage.all()["State." + _id].__dict__
        self.assertIn("name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            _id = f.getvalue().strip()
        cmd = "update City " + _id + " name" + " value"
        self.assertFalse(HBNBCommand().onecmd(cmd))
        attr = models.storage.all()["City." + _id].__dict__
        self.assertIn("name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            _id = f.getvalue().strip()
        cmd = "update Amenity " + _id + " name" + " value"
        self.assertFalse(HBNBCommand().onecmd(cmd))
        self.assertIn("name", models.storage.all()["Amenity." + _id].__dict__)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = f.getvalue().strip()
        cmd = "update Place " + _id + " name" + " value"
        self.assertFalse(HBNBCommand().onecmd(cmd))
        attr = models.storage.all()["Place." + _id].__dict__
        self.assertIn("name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            _id = f.getvalue().strip()
        cmd = "update Review " + _id + " name" + " value"
        self.assertFalse(HBNBCommand().onecmd(cmd))
        attr = models.storage.all()["Review." + _id].__dict__
        self.assertIn("name", attr)

    def test_update_objs_method(self):
        """This function tests the functionality of the update method"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = f.getvalue().strip()
        cmd = "BaseModel.update('{}', 'name', 'value')".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        attr = models.storage.all()["BaseModel." + _id].__dict__
        self.assertIn("name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = f.getvalue().strip()
        cmd = "User.update('{}', 'name', 'value')".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        attr = models.storage.all()["User." + _id].__dict__
        self.assertIn("name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            _id = f.getvalue().strip()
        cmd = "State.update('{}', 'name', 'value')".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        attr = models.storage.all()["State." + _id].__dict__
        self.assertIn("name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            _id = f.getvalue().strip()
        cmd = "City.update('{}', 'name', 'value')".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        attr = models.storage.all()["City." + _id].__dict__
        self.assertIn("name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            _id = f.getvalue().strip()
        cmd = "Amenity.update('{}', 'name', 'value')".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        attr = models.storage.all()["Amenity." + _id].__dict__
        self.assertIn("name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = f.getvalue().strip()
        cmd = "Place.update('{}', 'name', 'value')".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        attr = models.storage.all()["Place." + _id].__dict__
        self.assertIn("name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            _id = f.getvalue().strip()
        cmd = "Review.update('{}', 'name', 'value')".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        attr = models.storage.all()["Review." + _id].__dict__
        self.assertIn("name", attr)

    def test_update_int_method(self):
        """This function checks certain functionalities of update method"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = f.getvalue().strip()
        cmd = "update Place " + _id + " number_rooms" + " '7'"
        self.assertFalse(HBNBCommand().onecmd(cmd))
        _dict = models.storage.all()["Place." + _id].__dict__
        self.assertIs(type(_dict["number_rooms"]), int)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = f.getvalue().strip()
        cmd = "Place.update('{}', 'number_rooms', \"7\")".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        attr = models.storage.all()["Place." + _id].__dict__
        self.assertIs(type(_dict["number_rooms"]), int)

    def test_update_float_method(self):
        """This function checks certain functionalities of update method"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = f.getvalue().strip()
        cmd = "update Place " + _id + " latitude" + " 3.9"
        self.assertFalse(HBNBCommand().onecmd(cmd))
        _dict = models.storage.all()["Place." + _id].__dict__
        self.assertIs(type(_dict["latitude"]), float)

    def test_string_quotes_update(self):
        """This function tests certain functionalies of update function"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = f.getvalue().strip()
        cmd = "update User " + _id + " first_name" + " 'John Doe'"
        self.assertFalse(HBNBCommand().onecmd(cmd))
        _dict = models.storage.all()["User." + _id].__dict__
        self.assertEqual(_dict['first_name'], "John Doe")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = f.getvalue().strip()
        cmd = "User.update('{}', 'first_name', 'John Doe')".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        _dict = models.storage.all()["User." + _id].__dict__
        self.assertEqual(_dict['first_name'], "John Doe")

    def test_update_dict(self):
        """This function tests the functionality of update with a dict
        passed"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = f.getvalue().strip()
        cmd = "BaseModel.update('{}', {{'first_name': 'John'}})".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        attr = models.storage.all()["BaseModel." + _id].__dict__
        self.assertIn("first_name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = f.getvalue().strip()
        cmd = "User.update('{}', {{'name': 'value'}})".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        attr = models.storage.all()["User." + _id].__dict__
        self.assertIn("name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            _id = f.getvalue().strip()
        cmd = "State.update('{}', {{'name': 'value'}})".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        attr = models.storage.all()["State." + _id].__dict__
        self.assertIn("name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            _id = f.getvalue().strip()
        cmd = "City.update('{}', {{'name': 'value'}})".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        attr = models.storage.all()["City." + _id].__dict__
        self.assertIn("name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            _id = f.getvalue().strip()
        cmd = "Amenity.update('{}', {{'name': 'value'}})".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        attr = models.storage.all()["Amenity." + _id].__dict__
        self.assertIn("name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = f.getvalue().strip()
        cmd = "Place.update('{}', {{'name': 'value'}})".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        attr = models.storage.all()["Place." + _id].__dict__
        self.assertIn("name", attr)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            _id = f.getvalue().strip()
        cmd = "Review.update('{}', {{'name': 'value'}})".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        attr = models.storage.all()["Review." + _id].__dict__
        self.assertIn("name", attr)

    def test_update_invalid_dict(self):
        """This function tests for the response of update to invalid dict"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "BaseModel.update('{}', {{'first_name', 'John'}}".format(_id)
            line = HBNBCommand().precmd(cmd)
            self.assertFalse(HBNBCommand().onecmd(line))
            msg = "*** Unknown syntax: " + cmd
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "User.update('{}', {{'name', 'value'}})".format(_id)
            line = HBNBCommand().precmd(cmd)
            self.assertFalse(HBNBCommand().onecmd(line))
            msg = "*** Unknown syntax: " + cmd
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            _id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "State.update('{}', {{'name', 'value'}}".format(_id)
            line = HBNBCommand().precmd(cmd)
            self.assertFalse(HBNBCommand().onecmd(line))
            attr = models.storage.all()["State." + _id].__dict__
            msg = "*** Unknown syntax: " + cmd
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            _id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "City.update('{}', {{'name', 'value'}}".format(_id)
            line = HBNBCommand().precmd(cmd)
            self.assertFalse(HBNBCommand().onecmd(line))
            msg = "*** Unknown syntax: " + cmd
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            _id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "Amenity.update('{}', {{'name', 'value'}}".format(_id)
            line = HBNBCommand().precmd(cmd)
            self.assertFalse(HBNBCommand().onecmd(line))
            msg = "*** Unknown syntax: " + cmd
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "Place.update('{}', {{'name', 'value'}}".format(_id)
            line = HBNBCommand().precmd(cmd)
            self.assertFalse(HBNBCommand().onecmd(line))
            msg = "*** Unknown syntax: " + cmd
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            _id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            cmd = "Review.update('{}', {{'name' 'value'}})".format(_id)
            line = HBNBCommand().precmd(cmd)
            self.assertFalse(HBNBCommand().onecmd(line))
            msg = "*** Unknown syntax: " + cmd
            self.assertEqual(msg, f.getvalue().strip())

    def test_update_int_method_dict(self):
        """This function checks certain functionalities of update method"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = f.getvalue().strip()
        cmd = "Place.update('{}', {{'number_rooms': \"7\"}})".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        _dict = models.storage.all()["Place." + _id].__dict__
        self.assertIs(type(_dict["number_rooms"]), int)

    def test_update_float_method_dict(self):
        """This function checks certain functionalities of update method"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = f.getvalue().strip()
        cmd = "Place.update('{}', {{'latitude': 3.9}})".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        _dict = models.storage.all()["Place." + _id].__dict__
        self.assertIs(type(_dict["latitude"]), float)

    def test_string_quotes_update_dict(self):
        """This function tests certain functionalies of update function"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = f.getvalue().strip()
        cmd = "User.update('{}', {{'first_name': 'John Doe'}})".format(_id)
        line = HBNBCommand().precmd(cmd)
        self.assertFalse(HBNBCommand().onecmd(line))
        _dict = models.storage.all()["User." + _id].__dict__
        self.assertEqual(_dict['first_name'], "John Doe")


@unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "skip if storage type is db"
        )
class Test_count(unittest.TestCase):
    '''class test counting the number of instances'''
    @classmethod
    def setUpClass(cls):
        '''Remove the file/db at the beginning of the test'''
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            os.environ['HBNB_ENV'] = 'test'
        else:
            try:
                models.FileStorage._FileStorage__objects = {}
                os.remove(models.FileStorage._FileStorage__file_path)
            except FileNotFoundError:
                pass

    def setUp(self):
        '''Reset the `FileStorage.__objects`'''
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            os.environ['HBNB_ENV'] = 'test'
        else:
            try:
                models.FileStorage._FileStorage__objects = {}
                os.remove(models.FileStorage._FileStorage__file_path)
            except FileNotFoundError:
                pass

    def test_count_zero(self):
        '''Test there's number of counting instances printed'''
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count'))
            self.assertTrue(f.getvalue().strip().isnumeric())
            self.assertEqual(int(f.getvalue().strip()), 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count BaseModel'))
            self.assertEqual(int(f.getvalue().strip()), 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count User'))
            self.assertEqual(int(f.getvalue().strip()), 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count City'))
            self.assertEqual(int(f.getvalue().strip()), 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count Amenity'))
            self.assertEqual(int(f.getvalue().strip()), 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count Review'))
            self.assertEqual(int(f.getvalue().strip()), 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count State'))
            self.assertEqual(int(f.getvalue().strip()), 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count Place'))
            self.assertEqual(int(f.getvalue().strip()), 0)

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') == 'db',
            "skip if storage type is db"
            )
    def test_count_BaseModel(self):
        '''Test there's number of counting instances printed'''
        from models.base_model import BaseModel
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count BaseModel'))
            self.assertEqual(int(f.getvalue().strip()), 0)
        with patch("sys.stdout", new=StringIO()) as f:
            BaseModel().save()
            line = HBNBCommand().precmd('BaseModel.count()')
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(int(f.getvalue().strip()), 1)

    def test_count_User(self):
        '''Test count User'''
        from models.user import User
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count User'))
            self.assertEqual(int(f.getvalue().strip()), 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(
                    HBNBCommand().onecmd(
                        'create User email="test@test" password="test123"'
                        )
                    )
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count User'))
            count = f.getvalue().strip()
            self.assertEqual(int(count), 1)

    def test_count_City(self):
        '''Test count City'''
        from models.state import State
        from models.city import City
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count City'))
            self.assertEqual(int(f.getvalue().strip()), 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(
                    HBNBCommand().onecmd('create State name="Test_State"')
                    )
            state_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(
                    HBNBCommand().onecmd(
                        f'create City state_id="{state_id}" '
                        'name="Test_City"'
                        )
                    )
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count City'))
            self.assertEqual(int(f.getvalue().strip()), 1)

    def test_count_Amenity(self):
        '''Test count Amenity'''
        from models.amenity import Amenity
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count Amenity'))
            self.assertEqual(int(f.getvalue().strip()), 0)
        with patch("sys.stdout", new=StringIO()) as f:
            Amenity().save()
            line = HBNBCommand().precmd('Amenity.count()')
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(int(f.getvalue().strip()), 1)

    def test_count_State(self):
        '''Test count State'''
        from models.state import State
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count State'))
            self.assertEqual(int(f.getvalue().strip()), 0)
        with patch("sys.stdout", new=StringIO()) as f:
            State().save()
            line = HBNBCommand().precmd('State.count()')
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(int(f.getvalue().strip()), 1)

    def test_count_Review(self):
        '''Test count Review'''
        from models.review import Review
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count Review'))
            self.assertEqual(int(f.getvalue().strip()), 0)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(
                    HBNBCommand().onecmd(
                        'create User email="test@test" password="test123"'
                        )
                    )
            user_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(
                    HBNBCommand().onecmd('create State name="Kharotum"')
                    )
            state_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(
                    HBNBCommand().onecmd(
                        f'create City state_id="{state_id}" name="Bahry"'
                        )
                    )
            city_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(
                    HBNBCommand().onecmd(
                        f'create Place city_id="{city_id}" user_id="{user_id}"'
                        ' name="My_Place" description="A_lovely_place" '
                        'number_rooms=2 number_bathrooms=1 max_guest=2 '
                        'price_by_night=100 latitude=37.77 longitude=-122.41')
                    )
            place_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(
                    HBNBCommand().onecmd(
                        f'create Review place_id="{place_id}" '
                        f'user_id="{user_id}" text="Great place!"'
                        )
                    )
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count Review'))
            self.assertEqual(int(f.getvalue().strip()), 1)

    def test_count_Place(self):
        '''Test count Place'''
        from models.place import Place
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count Place'))
            self.assertEqual(int(f.getvalue().strip()), 0)
        with patch("sys.stdout", new=StringIO()) as f:
            Place().save()
            line = HBNBCommand().precmd('Place.count()')
            self.assertFalse(HBNBCommand().onecmd(line))
            self.assertEqual(int(f.getvalue().strip()), 1)

    def test_count_arg(self):
        '''Invalid arg'''
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('count arg'))
            self.assertEqual(int(f.getvalue().strip()), 0)


if __name__ == '__main__':
    unittest.main()
