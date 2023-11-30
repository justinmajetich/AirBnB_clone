import unittest
import console
import io
import sys
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.file_storage = FileStorage()

    def test_preloop(self):
        """Test preloop method"""
        self.file_storage.preloop()
        self.assertTrue(self.file_storage.prelooped)

    def test_precmd(self):
        """Test precmd method"""
        line = "create BaseModel"
        new_line = self.file_storage.precmd(line)
        self.assertEqual(new_line, line)


class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.backup = sys.stdout  # backup the original stdout
        self.stdout = io.StringIO()  # create a stream for stdout
        sys.stdout = self.stdout  # redirect stdout

    def tearDown(self):
        """Clean up test environment"""
        sys.stdout = self.backup  # restore original stdout

    def test_preloop(self):
        """Test preloop method"""
        console = console.HBNBCommand()
        console.preloop()
        output = self.stdout.getvalue()
        self.assertEqual(output, '(hbnb)\n')

    def test_precmd(self):
        """Test precmd method"""
        console = HBNBCommand()
        line = "create BaseModel"
        new_line = console.precmd(line)
        self.assertEqual(new_line, line)

    def test_preloop(self):
        """Test preloop method"""
        console = HBNBCommand()
        console.preloop()
        output = self.stdout.getvalue()
        self.assertEqual(output, '(hbnb)\n')


if __name__ == "__main__":
    unittest.main()
