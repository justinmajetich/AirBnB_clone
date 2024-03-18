#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from . import storage
import uuid


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id', str(uuid.uuid4()))
        User.email = kwargs.get('email', User.email)
        User.password = kwargs.get('password', User.password)
        User.first_name = kwargs.get('first_name', User.first_name)
        User.last_name = kwargs.get('last_name', User.last_name)
        super().__init__(*args, **kwargs)
        storage.new(self)
