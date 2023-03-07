#!/usr/bin/python3
import unittest
from models.user import User


class TestUserModel(unittest.TestCase):
    """Unit tests for User model."""

    def test_user_instance(self):
        """Test that User instance is created"""
        user = User()
        self.assertIsInstance(user, User)

if __name__ == "__main__":
    unittest.main()