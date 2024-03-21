#!/usr/bin/python3
"""This module tests the User class"""
from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class TestUser(TestBaseModel):
    """Tests the User class"""

    data = {
        "User.a074a108-04f8-4742-89f6-9d288345ec91": {
            "__class__": "User",
            "created_at": "2024-03-19T09:25:22.486363",
            "email": "gui@hbtn.io",
            "first_name": "Guillaume",
            "id": "a074a108-04f8-4742-89f6-9d288345ec91",
            "last_name": "Snow",
            "password": "guipwd",
            "updated_at": "2024-03-19T09:25:22.486695",
        }
    }

    def setUp(self) -> None:
        self.user = User(
            **self.data["User.a074a108-04f8-4742-89f6-9d288345ec91"]
        )

    def test_first_name(self):
        """Tests the `first_name` attribute of the User class"""
        self.assertEqual(type(self.user.first_name), str)

    def test_last_name(self):
        """Tests the `last_name` attribute of the User class"""
        self.assertEqual(type(self.user.last_name), str)

    def test_email(self):
        """Tests the `email` attribute of the User class"""
        self.assertEqual(type(self.user.email), str)

    def test_password(self):
        """Tests the `password` attribute of the User class"""
        self.assertEqual(type(self.user.password), str)
