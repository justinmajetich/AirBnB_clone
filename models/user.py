#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__()
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
