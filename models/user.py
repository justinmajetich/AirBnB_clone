#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import type_of_storage


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'

    if type_of_storage == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))

        places = relationship(
            'Place',
            cascade='all, delete',
            backref='user'
            )

        reviews = relationship(
            'Review',
            cascade='all, delete-orphan',
            backref='user'
            )
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
