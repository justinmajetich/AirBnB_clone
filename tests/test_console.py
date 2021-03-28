#!/usr/bin/python3
"""Console Unit Test"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel


# Dictionary to store available and known classes
class_list= ["BaseModel",
              "State",
              "City",
              "Amenity",
              "Place",
              "Review",
              "User"
              ]
# Dictionary storing all commands, used for default()
func_list = ["create()", "show", "destroy", "all", "update", "cowsay", "count"]


def reset(self):
    """Remove json file before starting a test"""
    try:
        os.remove("BaseModels.json")
    except:
        pass
    FileStorage.__objects = {}

class dummyTest(unittest.TestCase):
    """Dummy Test Cases for testing purposes, not real tests"""

    @classmethod
    def setup(self):
        """Remove json file before starting a test"""
        try:
            os.rename("BaseModels.json", "tmp")
        except:
            pass
        assertEquals("", FileStorage.__Objects)
        FileStorage.__objects = {}

    @classmethod
    def teardown(self):
        """Removing json file"""
        try:
            os.remove("BaseModels.json")
            models.storage.reload()
        except:
            pass
    
    def test_cmdPrompt(self):
        """idk"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")

# ----------------------CREATE---------------------------------------
    def test_help_create(self):
        """test help create"""
        answer = "USAGE: create [class], creates an instance of given class"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(answer, f.getvalue().strip())

    def test_create(self):
        """test create"""
        answer = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(answer, f.getvalue().strip())

    def test_create_fake_class(self):
        """test create fakeClass"""
        answer = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create fakeClass")
            self.assertEqual(answer, f.getvalue().strip())

    def test_create_all_classes_test(self):
        """test create all classes test"""
        for a in class_list:
            with patch('sys.stdout', new=StringIO()) as f:
                command = a
                HBNBCommand().onecmd("create {}".format(command))
                key = "{}.{}".format(command, f.getvalue().strip())
                self.assertIn(key, str(storage.all().keys()))
                self.assertEqual(None, HBNBCommand().onecmd("count {}".format(a)))

if __name__ == '__main__':
    unittest.main()