import unittest
from console import HBNBCommand

class TestCreateCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def test_create_with_string_param(self):
        self.console.do_create("BaseModel name=\"My_little_house\"")

    def test_create_with_float_param(self):
        self.console.do_create("BaseModel price=10.5")

    def test_create_with_int_param(self):
        self.console.do_create("BaseModel number=5")

    def test_create_with_invalid_param(self):
        self.console.do_create("BaseModel invalid_param")


if __name__ == "__main__":
    unittest.main()
