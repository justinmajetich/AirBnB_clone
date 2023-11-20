#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


s = "HBNB_TYPE_STORAGE"
if cs in environ.keys() and environ["HBNB_TYPE_STORAGE"] == 'db':
    class User(BaseModel, Base):
        """
        This is the class for user
        Attributes:
            email: email address
            password: login password
            first_name: first name
            last_name: last name
        """
        __tablename__ = "user"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", backref="user")
        reviews = relationship("Reviews", backref="user")

        def __init__(self, **kwargs):
            setattr(self, 'id', str(uuid4()))
            for k, v in kwargs.items():
                setattr(self, k, v)

class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
