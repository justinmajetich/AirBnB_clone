#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class User(BaseModel, Base):
    """Name of table in database to link to"""
    __tablename__ = 'users'

    """This class defines a user by various attributes"""
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    """Check if env variable is db(sql), if so create rel w/ place"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        places = relationship('Place', cascade='all, delete-orphan', backref='state')
        """If env variable is not db(sql), its FileStorage"""
    else:
        @property
        def places(self):
            from models import storage
            return [place for place in storage.all(Place).values() if place.user_id == self.id]