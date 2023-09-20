#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.review import Review
from models.place import Place


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    email = Column('email', String(128), nullable=False)
    password = Column('password', String(128), nullable=False)
    first_name = Column('first_name', String(128), nullable=True)
    last_name = Column('last_name', String(128), nullable=True)
    __tablename__ = 'users'
    places = relationship(
        'Place',
        backref='user',
        cascade='all, delete, delete-orphan'
    )
    reviews = relationship(
        'Review',
        backref='user',
        cascade='all, delete, delete-orphan'
    )
