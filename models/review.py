#!/usr/bin/python3

"""
A module that defines ORM class for Review table
"""
from os import getenv
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String
from models.base_model import Base, BaseModel


class Review(BaseModel, Base):
    """
    Defines attributes for Review table
    """
    __tablename__ = 'reviews'
<<<<<<< HEAD
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)


=======

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(
            String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(
            String(60), ForeignKey('users.id'), nullable=False)
    else:
        text = ''
        place_id = ''
        user_id = ''
>>>>>>> 1770a4fb53446035b89be39655c2c2913e9c6151
