import unittest
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.city import City
from console import HBNBCommand
import os


class TestConsole(unittest.TestCase):
    """Test suite for the console"""
    path_file = 'file.json'

    def setUp(self):
        """creates console object"""
        self.console = HBNBCommand()

    def test_do_create_1(self):
        """tests that a class object is created without args"""
        if os.path.isfile(self.path_file):
            os.system('rm file.json')
        os.system('echo "create User" | ./console.py')
        self.assertTrue(os.path.isfile(self.path_file))

    def test_do_create_2(self):
        """test that  class object is created when args are passed"""
        if os.path.isfile(self.path_file):
            os.system('rm file.json')
        os.system("echo 'create User name={}' | ./console.py".format('"Omar"'))
        self.assertTrue(os.path.isfile(self.path_file))

    def test_do_create_3(self):
        """test that class object is created when passing
        multiple number of arguments"""
        result = self.console.onecmd('create Place city_id="0001"\
                user_id="0001" name="My_little_house" number_rooms=4\
                number_bathrooms=2 max_guest=10 price_by_night=300\
                latitude=37.773972 longitude=-122.431297')
        self.assertTrue(os.path.isfile(self.path_file))
