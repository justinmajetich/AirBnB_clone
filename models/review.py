#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from models import dbstorage
from models.user import User
from models.place import Place

class Review(BaseModel, Base):
    """ Review class to store review information """
    __table__ = 'reviews'
    if dbstorage == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
