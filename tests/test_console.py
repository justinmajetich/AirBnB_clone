import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cli = HBNBCommand()

def test_do_create(self):
    with patch('sys.stdout', new=StringIO()) as f:
        self.cli.onecmd("create User name='John Doe' age=30")
    output = f.getvalue().strip()
    user_id = output.split()[0]  # extract the user ID from the output string
    self.assertIn(user_id, self.cli.onecmd("all User").split("\n"))  # split the output string into a list
    self.assertIn("'name': 'John Doe'", self.cli.onecmd("show User {}".format(user_id)))
    self.assertIn("'age': 30", self.cli.onecmd("show User {}".format(user_id)))

