#!/usr/bin/python3
import unittest
from unittest.mock import patch
import sys
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestHBNBCommand(unittest.TestCase):
    """
    Test the HBNBCommand class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class for the tests
        """
        cls.console = HBNBCommand()

    def setUp(self):
        """
        Set up method for each test
        """
        self.backup = sys.stdout
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        """
        Tear down method for each test
        """
        sys.stdout = self.backup

    def test_create(self):
        """
        Test the create command
        """
        self.console.onecmd("create BaseModel")
        self.assertTrue(len(storage.all()) > 0)

    def test_show(self):
        """
        Test the show command
        """
        instance = BaseModel()
        instance_id = instance.id
        self.console.onecmd("create BaseModel")
        self.console.onecmd(f"show BaseModel {instance_id}")
        output = self.output.getvalue().strip()
        self.assertIn(str(instance), output)

    def test_all(self):
        """
        Test the all command
        """
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create User")
        self.console.onecmd("all")
        output = self.output.getvalue().strip()
        self.assertIn(str(storage.all()), output)
        self.assertIn("[", output)
        self.assertIn("]", output)

    def test_all(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            HBNBCommand().onecmd("all")
            actual_output = fake_out.getvalue().strip()
            all_objects = storage.all()
            expected_output = "\n".join(
                obj.__class__.__name__ + "." + obj.id for obj in all_objects.values()
            )
            self.assertEqual(actual_output, expected_output)

    def test_update(self):
        new_user = User()
        new_user.save()
        with patch("sys.stdout", new=StringIO()) as fake_out:
            HBNBCommand().onecmd(
                "update User {} name 'Updated Name'".format(new_user.id)
            )
            updated_instance = storage.all()["User.{}".format(new_user.id)]
            self.assertEqual(updated_instance.name, "Updated Name")


if __name__ == "__main__":
    unittest.main()
