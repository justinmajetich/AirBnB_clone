import io
import sys
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cli = HBNBCommand()

    def test_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            id_ = f.getvalue().strip()

        self.assertTrue(id_ is not None)
        self.assertTrue(len(id_) > 0)

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            new_id = f.getvalue().strip()

        self.assertNotEqual(id_, new_id)

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd(f'show BaseModel {id_}')
            output = f.getvalue().strip()

        self.assertIn(id_, output)
        self.assertIn('BaseModel', output)

        self.cli.onecmd(f'destroy BaseModel {id_}')
        self.cli.onecmd(f'destroy BaseModel {new_id}')

    def test_do_show(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd("create Place")
            id_ = f.getvalue().strip()

        self.assertTrue(id_ is not None)
        self.assertTrue(len(id_) > 0)

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd(f"show Place {id_}")
            expected_output = f.getvalue().strip()

        self.assertIn(id_, expected_output)

        self.cli.onecmd(f'destroy Place {id_}')

    def test_do_destroy(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd("create Place")
            id_ = f.getvalue().strip()

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd("destroy")
            output = f.getvalue().strip()

        self.assertIn("** class name missing **", output)

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd("destroy NewClass")
            output = f.getvalue().strip()

        self.assertIn("** class doesn't exist **", output)

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd("destroy Place")
            output = f.getvalue().strip()

        self.assertIn("** instance id missing **", output)

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd("destroy Place 1243")
            output = f.getvalue().strip()

        self.assertIn("** no instance found **", output)

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd("destroy Place 1243")
            output = f.getvalue().strip()

        self.assertIn("** no instance found **", output)

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd(f"destroy Place {id_}")
            output = f.getvalue().strip()

        self.assertIn("", output)

    def test_do_count(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            id_ = f.getvalue().strip()

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            new_id = f.getvalue().strip()

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.cli.onecmd(f"count BaseModel")
            output = f.getvalue().strip()

        self.assertEqual(2, int(output))

        self.cli.onecmd(f"destroy BaseModel {id_}")
        self.cli.onecmd(f"destroy BaseModel {new_id}")
