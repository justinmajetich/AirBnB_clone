import unittest
import os
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up the HBNBCommand instance for testing"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up resources after testing"""
        del self.console

    def test_create_command(self):
        """Test the create command"""
        with StringIO() as out, StringIO() as err:
            sys.stdout = out
            sys.stderr = err
            self.console.onecmd("create State name='California'")
            output = out.getvalue().strip()
            self.assertIn("0706bf0f-a147-400e-a6f7-c1e736698125", output)
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

    def test_show_command(self):
        """Test the show command"""
        with StringIO() as out, StringIO() as err:
            sys.stdout = out
            sys.stderr = err
            self.console.onecmd("create State name='California'")
            self.console.onecmd(
                    "show State 0706bf0f-a147-400e-a6f7-c1e736698125"
            )
            output = out.getvalue().strip()
            self.assertIn("name: California", output)
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__


if __name__ == "__main__":
    unittest.main()
