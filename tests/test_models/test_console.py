import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cli = HBNBCommand()

    def tearDown(self):
        self.cli = None

    def test_quit(self):
        with self.assertRaises(SystemExit):
            self.cli.do_quit(None)

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        self.cli.do_help(None)
        output = mock_stdout.getvalue()
        self.assertIn("Documented commands (type help <topic>):", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        self.cli.do_create("User name='John Doe' age=30")
        output = mock_stdout.getvalue()
        self.assertTrue(len(output) > 0)
        self.assertTrue(output.startswith("b"))
        # replace newline and b' character
        output = output.replace("\n", "").replace("b'", "").replace("'", "")
        self.assertTrue(len(output) == 36)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        self.cli.do_show("User " + "123456")
        output = mock_stdout.getvalue()
        self.assertIn("** no instance found **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        self.cli.do_destroy("User " + "123456")
        output = mock_stdout.getvalue()
        self.assertIn("** no instance found **", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        self.cli.do_all("User")
        output = mock_stdout.getvalue()
        self.assertEqual("[[], []]\n", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        self.cli.do_count("User")
        output = mock_stdout.getvalue()
        self.assertEqual("0\n", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        self.cli.do_update("User " + "123456")
        output = mock_stdout.getvalue()
        self.assertIn("** no instance found **", output)


if __name__ == '__main__':
    unittest.main()
