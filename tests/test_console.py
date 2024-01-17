import unittest
import sys
import os
from io import StringIO
import uuid
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

            # Extract the generated UUID from the output
            generated_uuid = output.split()[-1]

            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

            return generated_uuid

    def test_show_command(self):
        """Test the show command"""
        pass
        """
            with StringIO() as out, StringIO() as err:
            sys.stdout = out
            sys.stderr = err

            # Get the generated UUID from the create command
            generated_uuid = self.test_create_command()

            self.console.onecmd(f"show State {generated_uuid}")
            output = out.getvalue().strip()
            self.assertIn("name: California", output)

            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
        """


if __name__ == "__main__":
    unittest.main()
