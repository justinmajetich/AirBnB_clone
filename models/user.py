#!/usr/bin/python3
"""This module defines a class User"""
from models import storage
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy.orm import relationship


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    places = relationship("Place", backref="user")
