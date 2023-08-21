#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship(
                'Place', backref='user', cascade='all, delete'
                )
        review = relationship('Review', backref='user', cascade='all, delete')

    else:
        @property
        def places(self):
            """Getter attribute in case of file storage"""
            places_list = []
            for place in models.storage.all(Place).values():
                if place.user_id == self.id:
                    places_list.append(place)
            return places_list
