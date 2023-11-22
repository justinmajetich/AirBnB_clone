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
        filtered_kwargs = {k: v for k, v in kwargs.items() if hasattr(self, k) or k == "id"}
        super().__init__(*args, **filtered_kwargs)
