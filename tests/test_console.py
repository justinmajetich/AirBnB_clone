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

    def test_create(self):
        id_ = self.capture_stdout("create BaseModel")
        self.assertTrue(id_ is not None)
        self.assertTrue(len(id_) > 0)

        new_id = self.capture_stdout("create BaseModel")
        self.assertNotEqual(id_, new_id)

        output = self.capture_stdout(f'show BaseModel {id_}')
        self.assertIn(id_, output)
        self.assertIn('BaseModel', output)

        self.cli.onecmd(f'destroy BaseModel {id_}')
        self.cli.onecmd(f'destroy BaseModel {new_id}')


if __name__ == '__main__':
    unittest.main()
