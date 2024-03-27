#!/usr/bin/python3
""" Review module for the HBNB project """
from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Review(BaseModel, Base):
        """ Review classto store review information """
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
else:
    class Review(BaseModel):
        """ Review classto store review information """
        place_id = ""
        user_id = ""
        text = ""
