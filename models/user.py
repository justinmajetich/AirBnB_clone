#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base

from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__="users"
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    place = relationship("Place", backref='user', cascade="delete")
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
