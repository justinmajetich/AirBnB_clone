#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    valid_attr = ['email', 'password', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(User, self).__init__()
        for key in self.valid_attr:
            if key in kwargs:
                setattr(self, key, kwargs[key])
