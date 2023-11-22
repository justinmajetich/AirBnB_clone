import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel


class TestHBNBCommandCreate(unittest.TestCase):
    def setUp(self):
        """Set up the HBNBCommand instance and reditect stdout for testing."""
        self.hbnb_command = HBNBCommand()
        self.stdout_backup = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        """Restore original stdout."""
        sys.stdout = self.stdout_backup

    @patch('models.storage')
    def test_do_create_valid(self, mock_storage):
        """Test do_create with valid arguments."""
        with patch('builtins.input', return_value="BaseModel") as mock_input:
            self.hbnb_command.do_create('')
            output = sys.stdout.getvalue().strip()
            self.assertTrue(mock_storage.new.called)
            self.assertIn('created', output.lower())
            self.assertIn('BaseModel', output)

    def test_do_create_missing_class(self):
        """Test do_create with missing class name."""
        with patch('builtins.input', return_value='') as mock_input:
            self.hbnb_command.do_create('')
            output = sys.stdout.getvalue().strip()
            self.assertIn('class name missing', output.lower())

    def test_do_create_invalid_class(self):
        """Test do_create with invalid class name."""
        with patch('builtins.input', return_value='InvalidClass')\
                as mock_input:
            self.hbnb_command.do_create('')
            output = sys.stdout.getvalue().strip()
            self.assertIn("class 'InvalidClass' doesn't exist", output.lower())

    def test_do_create_with_args(self):
        """Test do_create with arguments."""
        with patch('builtins.input', return_value='BaseModel key="value"')\
                as mock_input:
            self.hbnb_command.do_create('')
            output = sys.stdout.getvalue().strip()
            self.assertTrue(mock_storage.new.called)
            self.assertIn('created', output.lower())
            self.assertIn('BaseModel', output)
            self.assertIn('key', output)
            self.assertIn('value', output)


if __name__ == '__main__':
    unittest.main()
