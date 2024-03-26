#!/usr/bin/python3
import unittest
import json
from console import HBNBCommand
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO
import os
import sys


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        from console import HBNBCommand
        self.console = HBNBCommand()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    @patch("sys.stdout", new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout, function, *args):
        function(*args)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_create_state_present(self):
        """Test create State is present (regular case)"""
        with patch("sys.stdin", StringIO("create State\nquit\n")):
            self.assert_stdout("(hbnb) \n(hbnb) \n", self.console.cmdloop)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "No apply for db")
    def test_create_state_name(self):
        """Test create State name=California"""
        with patch("sys.stdin", StringIO("create \
                                         State name=\"California\"\nquit\n")):
            self.assert_stdout("(hbnb) \n(hbnb) \n", self.console.cmdloop)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "No apply for db")
    def test_create_state_city(self):
        """Test create State name="California" + create City
        state_id="<new state ID>" name=San_Francisco"""
        with patch("sys.stdin", StringIO("create \
                                         State name=\"California\"\ncreate \
                                         City state_id=\"<new state ID>\" \
                                         name=\"San_Francisco\"\nquit\n")):
            self.assert_stdout("(hbnb) \n(hbnb) \
                               \n(hbnb) \n", self.console.cmdloop)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "No apply for db")
    def test_create_state_multiple_cities(self):
        """Test create State name="California" + \
            create City state_id="<new state ID>" name=Fremont"""
        with patch("sys.stdin", StringIO("create \
                                         State name=\"California\"\ncreate \
                                         City state_id=\"<new state ID>\" \
                                         name=\"Fremont\"\nquit\n")):
            self.assert_stdout("(hbnb) \n(hbnb) \n(hbnb)\
                                \n", self.console.cmdloop)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "No apply for db")
    def test_create_state_city_user_place(self):
        """Test create State name="California" + create City \
            state_id="<new state ID>" name="San_Francisco_is_super_cool" \
                + create User email="my@me.com" password="pwd" \
                    first_name="FN" \
                    last_name="LN" + create Place \
                        city_id="<new city ID>" user_id="<new user ID>" \
                        name="My_house" description="no_description_yet"\
                              number_rooms=4 \
                            number_bathrooms=1 max_guest=3 \
                                price_by_night=100 latitude=120.12\
                                  longitude=101.4 + show Place \
                                    <new place ID>"""
        commands = [
            "create State name=\"California\"\n",
            "create City state_id=\"<new state ID>\" \
                name=\"San_Francisco_is_super_cool\"\n",
            "create User email=\"my@me.com\" \
                password=\"pwd\" first_name=\"FN\" \
                last_name=\"LN\"\n",
            "create Place city_id=\"<new city ID>\" user_id=\"<new user ID>\" \
            name=\"My_house\" description=\"no_description_yet\" \
                number_rooms=4 number_bathrooms=1 max_guest=3 \
                    price_by_night=100 \
                    latitude=120.12 longitude=101.4\n",
            "show Place <new place ID>\n",
            "quit\n"
        ]
        with patch("sys.stdin", StringIO("".join(commands))):
            self.assert_stdout(
                "(hbnb) \n(hbnb) \n(hbnb) \n(hbnb) \n(hbnb) \
                    \n(hbnb) \n", self.console.cmdloop)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "No apply for db")
    def test_all(self):
        """Test all command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all asdfsdfsd")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all State")
            self.assertEqual("[]\n", f.getvalue())

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "No apply for db")
    def test_create(self):
        """Test create command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create asdfsfsd")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            self.assertEqual(
                '["[User', f.getvalue()[:7])

    def test_filestorage(self):
        """Test FileStorage functionality"""
        storage = FileStorage()
        state = State()
        city = City()
        place = Place()
        user = User()
        review = Review()
        amenity = Amenity()
        
        # Add objects to storage
        storage.new(state)
        storage.new(city)
        storage.new(place)
        storage.new(user)
        storage.new(review)
        storage.new(amenity)

        # Save objects to file
        storage.save()

        # Clear current storage
        storage._FileStorage__objects = {}

        # Reload objects from file
        storage.reload()

        # Check if objects were loaded correctly
        self.assertTrue(len(storage.all(State)) == 1)
        self.assertTrue(len(storage.all(City)) == 1)
        self.assertTrue(len(storage.all(Place)) == 1)
        self.assertTrue(len(storage.all(User)) == 1)
        self.assertTrue(len(storage.all(Review)) == 1)
        self.assertTrue(len(storage.all(Amenity)) == 1)


if __name__ == "__main__":
    unittest.main()
