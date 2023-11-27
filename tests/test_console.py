import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.state import State
from models.place import Place

class TestConsole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setup for the test cases."""
        cls.console = HBNBCommand()
        cls.obj_list = []
        cls.obj_list.append(BaseModel())
        cls.obj_list.append(State(name="California"))
        cls.obj_list.append(Place(city_id="0001", user_id="0001", name="My_little_house", number_rooms=4, number_bathrooms=2, max_guest=10, price_by_night=300, latitude=37.773972, longitude=-122.431297))

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command(self, mock_stdout):
        with patch('sys.stdin', StringIO("create BaseModel\nall\n")):
            self.console.cmdloop()
            output = mock_stdout.getvalue().strip()
            self.assertIn(str(self.obj_list[0]), output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command_with_params(self, mock_stdout):
        with patch('sys.stdin', StringIO("create State name=\"California\"\nall State\n")):
            self.console.cmdloop()
            output = mock_stdout.getvalue().strip()
            self.assertIn("California", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command_with_complex_params(self, mock_stdout):
        with patch('sys.stdin', StringIO("create Place city_id=\"0001\" user_id=\"0001\" name=\"My_little_house\" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297\nall Place\n")):
            self.console.cmdloop()
            output = mock_stdout.getvalue().strip()
            self.assertIn("My little house", output)
            self.assertIn("37.773972", output)

if __name__ == '__main__':
    unittest.main()
