import io
import sys
import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cli = HBNBCommand()

    def capture_stdout(self, command):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.cli.onecmd(command)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip()

    def test_do_create_base_model(self):
        command = "create BaseModel"
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd(command)
            output = f.getvalue().strip()

        self.assertTrue(len(output) > 0)

    def test_do_create_user_with_attributes(self):
        command = "create User email=\"test@example.com\" password=\"test\""
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd(command)
            output = f.getvalue().strip()

        self.assertTrue(len(output) > 0)

    def test_do_create_invalid_class_name(self):
        command = "create InvalidClass"
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd(command)
            output = f.getvalue().strip()

        self.assertEqual(output, "** class doesn't exist **")

    def test_do_create_missing_class_name(self):
        command = "create"
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd(command)
            output = f.getvalue().strip()

        self.assertEqual(output, "** class name missing **")


if __name__ == '__main__':
    unittest.main()
