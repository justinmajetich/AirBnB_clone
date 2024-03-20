#!/usr/bin/python3
"""Unit tests for the User class."""

# Importing necessary modules
from tests.test_models.test_base_model import test_basemodel
from models.user import User

class TestUserAttributes(test_basemodel):
    """Test cases for the attributes of the User class."""
    
    def __init__(self, *args, **kwargs):
        """Initialize test cases."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name_type(self):
        """Test if the 'first_name' attribute is of type string."""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name_type(self):
        """Test if the 'last_name' attribute is of type string."""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email_type(self):
        """Test if the 'email' attribute is of type string."""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password_type(self):
        """Test if the 'password' attribute is of type string."""
        new = self.value()
        self.assertEqual(type(new.password), str)
