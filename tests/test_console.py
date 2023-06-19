import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        # Mock the input arguments
        args = "State name='California'"

        # Call the do_create method
        self.console.do_create(args)

        # Get the output
        output = mock_stdout.getvalue().strip()

        # Assert the output
        self.assertIn("California", output)

if __name__ == '__main__':
    unittest.main()

