#!/usr/bin/python3
"""This is the user class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review
from os import getenv


class User(BaseModel, Base):
    """This is the class for user"""
    __tablename__ = "users"

    if getenv('HBNB_TYPE_STORAGE') is not None:

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", cascade='all, delete, delete-orphan',
                              backref="user", passive_deletes=True)
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="user", passive_deletes=True)

    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
