#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class User(BaseModel, Base):
        """Name of table in database to link to"""
        __tablename__ = 'users'

        """This class defines a user by various attributes"""
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')

        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')
else:
    class User(BaseModel):
        """This class defines a user by various attributes"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''
