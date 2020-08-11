#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    """needs to inherit from base (task six, update basemodel)"""

    """
   Add or replace in the class User:
        class attribute __tablename__
        represents the table name, users
   class attribute email
        represents a column containing a string (128 characters)
        can’t be null
   class attribute password
        represents a column containing a string (128 characters)
        can’t be null
   class attribute first_name
        represents a column containing a string (128 characters)
        can be null
   class attribute last_name
        represents a column containing a string (128 characters)
        can be null
""" 
