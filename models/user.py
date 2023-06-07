#!/usr/bin/python3
"""
Define the ``User`` class that inherits from the class ``BaseModel``
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Define the class User
    """

    email = str()
    password = str()
    first_name = str()
    last_name = str()
