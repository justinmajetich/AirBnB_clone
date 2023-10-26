import unittest
from unittest.mock import patch
from io import StringIO
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from console import HBNBCommand
import os
import sys


class Test_console(unittest.TestCase):
    """Test for console"""

    def test_do_create(self):
        """To test do_create in the console"""
        console = HBNBCommand()
        value = "create State name='Anambra'"

        # output = "State"
        HBNBCommand.classes = {'State': State}

        with patch('sys.stdout', new=StringIO()) as res:
            console.onecmd(value)
            self.assertTrue('State', res.getvalue().strip())
